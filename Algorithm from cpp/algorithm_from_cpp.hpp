#include <algorithm>
#include <chrono>
#include <functional>
#include <map>
#include <unordered_map>
#include <numeric>
#include <random>
#include <vector>

std::vector<std::vector<int> > LouvainCommunityDetect(std::vector<std::vector<int> > Edge,int node_num);
std::vector<std::vector<int> > LabelPropagation(std::vector<std::vector<int> > Edge,int node_num);