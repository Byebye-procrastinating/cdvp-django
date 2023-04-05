import docker
import os
from datetime import datetime
import tarfile
from io import BytesIO


def build_docker_for_py(file):
    client = docker.from_env()
    now = str(datetime.now()).replace(' ', '_').replace('.', '_').replace(':', '_')
    dir_name, full_file_name = os.path.split(file)
    Dockerfile_template = f"""FROM cdvp_python_docker
WORKDIR /{now}
COPY . .
RUN  pipreqs . && pip install -r requirements.txt
CMD ["python", "main.py"]
    """
    print(now, dir_name)
    open(dir_name + "/Dockerfile", 'w').write(Dockerfile_template)
    docker_image, logs = client.images.build(path=dir_name, tag='cdvp_python_docker:' + now)
    print(docker_image)
    image_id = docker_image.attrs.get('Id')
    print(f'Image ID: {image_id}')
    current_dir = dir_name
    container_path = f"/{now}"
    docker_container = client.containers.run(image_id, detach=True)
    docker_container.wait()
    data, _ = docker_container.get_archive(f'/{now}/output')

    stream = BytesIO()
    for chunk in data:
        stream.write(chunk)

    stream.seek(0)
    with tarfile.open(fileobj=stream, mode='r|') as tar:
        tar.extractall(path=dir_name)

    docker_container.stop()
    docker_container.remove()
    client.images.remove(image_id)

    return eval(open(dir_name + "/output", 'r').read())


if __name__ == '__main__':
    file = r'/home/alv/docker_learn/test_python/test.py'
    dataset = r'/home/alv/docker_learn/test_python/dataset'
    print(build_docker_for_py(file, dataset))
