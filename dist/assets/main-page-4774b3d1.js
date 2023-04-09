import{i as Me,s as ue,f as $e,a as Ae,b as de,c as Le,r as E,d as z,u as e,w as D,o as me,e as Oe,g as Pe,p as Re,h as Be,j as he,k as G,l as fe,m as T,n as M,q as d,t as oe,v as R,x as X,y as P,z as F,A as B,E as ne,B as ze,C as q,T as ie,D as x,F as We,G as pe,H as ve,I as Y,J as Z,K as ge,_ as ye,L as we,M as Ve,N as He,O as Ue,P as De,Q as Fe,R as xe,S as je,U as Ke,V as Xe,W as qe,X as re}from"./index-95382269.js";import{d as Ge}from"./debounce-b73110e2.js";var Je="Expected a function";function le(a,p,o){var s=!0,f=!0;if(typeof a!="function")throw new TypeError(Je);return Me(o)&&(s="leading"in o?!!o.leading:s,f="trailing"in o?!!o.trailing:f),Ge(a,p,{leading:s,maxWait:p,trailing:f})}const Qe=(a,p,o)=>$e(a.subTree).filter(l=>{var t;return Ae(l)&&((t=l.type)==null?void 0:t.name)===p&&!!l.component}).map(l=>l.component.uid).map(l=>o[l]).filter(l=>!!l),Ye=(a,p)=>{const o={},s=ue([]);return{children:s,addChild:t=>{o[t.uid]=t,s.value=Qe(a,p,o)},removeChild:t=>{delete o[t],s.value=s.value.filter(m=>m.uid!==t)}}},Ze=de({initialIndex:{type:Number,default:0},height:{type:String,default:""},trigger:{type:String,values:["hover","click"],default:"hover"},autoplay:{type:Boolean,default:!0},interval:{type:Number,default:3e3},indicatorPosition:{type:String,values:["","none","outside"],default:""},arrow:{type:String,values:["always","hover","never"],default:"hover"},type:{type:String,values:["","card"],default:""},loop:{type:Boolean,default:!0},direction:{type:String,values:["horizontal","vertical"],default:"horizontal"},pauseOnHover:{type:Boolean,default:!0}}),et={change:(a,p)=>[a,p].every(Le)},_e=Symbol("carouselContextKey"),ce=300,tt=(a,p,o)=>{const{children:s,addChild:f,removeChild:l}=Ye(he(),"ElCarouselItem"),t=E(-1),m=E(null),v=E(!1),y=E(),I=z(()=>a.arrow!=="never"&&!e(N)),C=z(()=>s.value.some(n=>n.props.label.toString().length>0)),g=z(()=>a.type==="card"),N=z(()=>a.direction==="vertical"),$=le(n=>{i(n)},ce,{trailing:!0}),S=le(n=>{W(n)},ce);function k(){m.value&&(clearInterval(m.value),m.value=null)}function A(){a.interval<=0||!a.autoplay||m.value||(m.value=setInterval(()=>V(),a.interval))}const V=()=>{t.value<s.value.length-1?t.value=t.value+1:a.loop&&(t.value=0)};function i(n){if(Be(n)){const H=s.value.filter(K=>K.props.name===n);H.length>0&&(n=s.value.indexOf(H[0]))}if(n=Number(n),Number.isNaN(n)||n!==Math.floor(n))return;const b=s.value.length,O=t.value;n<0?t.value=a.loop?b-1:0:n>=b?t.value=a.loop?0:b-1:t.value=n,O===t.value&&c(O),ee()}function c(n){s.value.forEach((b,O)=>{b.translateItem(O,t.value,n)})}function r(n,b){var O,H,K,te;const U=e(s),se=U.length;if(se===0||!n.states.inStage)return!1;const Ie=b+1,ke=b-1,ae=se-1,Ee=U[ae].states.active,Te=U[0].states.active,Ne=(H=(O=U[Ie])==null?void 0:O.states)==null?void 0:H.active,Se=(te=(K=U[ke])==null?void 0:K.states)==null?void 0:te.active;return b===ae&&Te||Ne?"left":b===0&&Ee||Se?"right":!1}function w(){v.value=!0,a.pauseOnHover&&k()}function L(){v.value=!1,A()}function h(n){e(N)||s.value.forEach((b,O)=>{n===r(b,O)&&(b.states.hover=!0)})}function u(){e(N)||s.value.forEach(n=>{n.states.hover=!1})}function _(n){t.value=n}function W(n){a.trigger==="hover"&&n!==t.value&&(t.value=n)}function J(){i(t.value-1)}function Ce(){i(t.value+1)}function ee(){k(),A()}D(()=>t.value,(n,b)=>{c(b),b>-1&&p("change",n,b)}),D(()=>a.autoplay,n=>{n?A():k()}),D(()=>a.loop,()=>{i(t.value)}),D(()=>a.interval,()=>{ee()}),D(()=>s.value,()=>{s.value.length>0&&i(a.initialIndex)});const Q=ue();return me(()=>{Q.value=Oe(y.value,()=>{c()}),A()}),Pe(()=>{k(),y.value&&Q.value&&Q.value.stop()}),Re(_e,{root:y,isCardType:g,isVertical:N,items:s,loop:a.loop,addItem:f,removeItem:l,setActiveItem:i}),{root:y,activeIndex:t,arrowDisplay:I,hasLabel:C,hover:v,isCardType:g,items:s,handleButtonEnter:h,handleButtonLeave:u,handleIndicatorClick:_,handleMouseEnter:w,handleMouseLeave:L,setActiveItem:i,prev:J,next:Ce,throttledArrowClick:$,throttledIndicatorHover:S}},st=["onMouseenter","onClick"],at={key:0},ot="ElCarousel",nt=G({name:ot}),it=G({...nt,props:Ze,emits:et,setup(a,{expose:p,emit:o}){const s=a,{root:f,activeIndex:l,arrowDisplay:t,hasLabel:m,hover:v,isCardType:y,items:I,handleButtonEnter:C,handleButtonLeave:g,handleIndicatorClick:N,handleMouseEnter:$,handleMouseLeave:S,setActiveItem:k,prev:A,next:V,throttledArrowClick:i,throttledIndicatorHover:c}=tt(s,o),r=fe("carousel"),w=z(()=>{const h=[r.b(),r.m(s.direction)];return e(y)&&h.push(r.m("card")),h}),L=z(()=>{const h=[r.e("indicators"),r.em("indicators",s.direction)];return e(m)&&h.push(r.em("indicators","labels")),(s.indicatorPosition==="outside"||e(y))&&h.push(r.em("indicators","outside")),h});return p({setActiveItem:k,prev:A,next:V}),(h,u)=>(T(),M("div",{ref_key:"root",ref:f,class:P(e(w)),onMouseenter:u[6]||(u[6]=F((..._)=>e($)&&e($)(..._),["stop"])),onMouseleave:u[7]||(u[7]=F((..._)=>e(S)&&e(S)(..._),["stop"]))},[d("div",{class:P(e(r).e("container")),style:ve({height:h.height})},[e(t)?(T(),oe(ie,{key:0,name:"carousel-arrow-left",persisted:""},{default:R(()=>[X(d("button",{type:"button",class:P([e(r).e("arrow"),e(r).em("arrow","left")]),onMouseenter:u[0]||(u[0]=_=>e(C)("left")),onMouseleave:u[1]||(u[1]=(..._)=>e(g)&&e(g)(..._)),onClick:u[2]||(u[2]=F(_=>e(i)(e(l)-1),["stop"]))},[B(e(ne),null,{default:R(()=>[B(e(ze))]),_:1})],34),[[q,(h.arrow==="always"||e(v))&&(s.loop||e(l)>0)]])]),_:1})):x("v-if",!0),e(t)?(T(),oe(ie,{key:1,name:"carousel-arrow-right",persisted:""},{default:R(()=>[X(d("button",{type:"button",class:P([e(r).e("arrow"),e(r).em("arrow","right")]),onMouseenter:u[3]||(u[3]=_=>e(C)("right")),onMouseleave:u[4]||(u[4]=(..._)=>e(g)&&e(g)(..._)),onClick:u[5]||(u[5]=F(_=>e(i)(e(l)+1),["stop"]))},[B(e(ne),null,{default:R(()=>[B(e(We))]),_:1})],34),[[q,(h.arrow==="always"||e(v))&&(s.loop||e(l)<e(I).length-1)]])]),_:1})):x("v-if",!0),pe(h.$slots,"default")],6),h.indicatorPosition!=="none"?(T(),M("ul",{key:0,class:P(e(L))},[(T(!0),M(Y,null,Z(e(I),(_,W)=>(T(),M("li",{key:W,class:P([e(r).e("indicator"),e(r).em("indicator",h.direction),e(r).is("active",W===e(l))]),onMouseenter:J=>e(c)(W),onClick:F(J=>e(N)(W),["stop"])},[d("button",{class:P(e(r).e("button"))},[e(m)?(T(),M("span",at,ge(_.props.label),1)):x("v-if",!0)],2)],42,st))),128))],2)):x("v-if",!0)],34))}});var rt=ye(it,[["__file","/home/runner/work/element-plus/element-plus/packages/components/carousel/src/carousel.vue"]]);const lt=de({name:{type:String,default:""},label:{type:[String,Number],default:""}}),ct=(a,p)=>{const o=we(_e),s=he(),f=.83,l=E(!1),t=E(0),m=E(1),v=E(!1),y=E(!1),I=E(!1),C=E(!1),{isCardType:g,isVertical:N}=o;function $(i,c,r){const w=r-1,L=c-1,h=c+1,u=r/2;return c===0&&i===w?-1:c===w&&i===0?r:i<L&&c-i>=u?r+1:i>h&&i-c>=u?-2:i}function S(i,c){var r;const w=((r=o.root.value)==null?void 0:r.offsetWidth)||0;return I.value?w*((2-f)*(i-c)+1)/4:i<c?-(1+f)*w/4:(3+f)*w/4}function k(i,c,r){const w=o.root.value;return w?((r?w.offsetHeight:w.offsetWidth)||0)*(i-c):0}const A=(i,c,r)=>{var w;const L=e(g),h=(w=o.items.value.length)!=null?w:Number.NaN,u=i===c;!L&&!Ue(r)&&(C.value=u||i===r),!u&&h>2&&o.loop&&(i=$(i,c,h));const _=e(N);v.value=u,L?(I.value=Math.round(Math.abs(i-c))<=1,t.value=S(i,c),m.value=e(v)?1:f):t.value=k(i,c,_),y.value=!0};function V(){if(o&&e(g)){const i=o.items.value.findIndex(({uid:c})=>c===s.uid);o.setActiveItem(i)}}return me(()=>{o.addItem({props:a,states:Ve({hover:l,translate:t,scale:m,active:v,ready:y,inStage:I,animating:C}),uid:s.uid,translateItem:A})}),He(()=>{o.removeItem(s.uid)}),{active:v,animating:C,hover:l,inStage:I,isVertical:N,translate:t,isCardType:g,scale:m,ready:y,handleItemClick:V}},ut=G({name:"ElCarouselItem"}),dt=G({...ut,props:lt,setup(a){const p=a,o=fe("carousel"),{active:s,animating:f,hover:l,inStage:t,isVertical:m,translate:v,isCardType:y,scale:I,ready:C,handleItemClick:g}=ct(p),N=z(()=>{const S=`${`translate${e(m)?"Y":"X"}`}(${e(v)}px)`,k=`scale(${e(I)})`;return{transform:[S,k].join(" ")}});return($,S)=>X((T(),M("div",{class:P([e(o).e("item"),e(o).is("active",e(s)),e(o).is("in-stage",e(t)),e(o).is("hover",e(l)),e(o).is("animating",e(f)),{[e(o).em("item","card")]:e(y)}]),style:ve(e(N)),onClick:S[0]||(S[0]=(...k)=>e(g)&&e(g)(...k))},[e(y)?X((T(),M("div",{key:0,class:P(e(o).e("mask"))},null,2)),[[q,!e(s)]]):x("v-if",!0),pe($.$slots,"default")],6)),[[q,e(C)]])}});var be=ye(dt,[["__file","/home/runner/work/element-plus/element-plus/packages/components/carousel/src/carousel-item.vue"]]);const mt=De(rt,{CarouselItem:be}),ht=Fe(be);const ft="/assets/a1-e4a864fb.png",pt="/assets/a2-6f9f984b.png";const j=a=>(Ke("data-v-3b3b7ff5"),a=a(),Xe(),a),vt={class:"main"},gt={class:"main-page-content"},yt={class:"left"},wt=j(()=>d("img",{src:qe,class:"img"},null,-1)),_t=j(()=>d("div",{class:"title"},"CDVP",-1)),bt=j(()=>d("div",{class:"des"},[re(" 为"),d("strong",null,"开发者"),re("打造的"),d("strong",null,"演示文档工具")],-1)),Ct={class:"btn"},It=j(()=>d("div",{class:"right"},[d("img",{src:ft,class:"img1"}),d("img",{src:pt,class:"img2"})],-1)),kt={class:"paper"},Et={class:"paper-left"},Tt=["src"],Nt={class:"paper-right"},St=j(()=>d("h1",null,"Describe",-1)),Mt={style:{padding:"5vh 2vw 5vh 2vw","font-size":"2vh","white-space":"pre-wrap"}},$t={__name:"main-page",setup(a){const p=E(),o=je(),s=we("activeIndex"),f=[{img:new URL("/assets/paper1-5236656d.png",self.location).href,des:"    Community detection remains an important problem in data mining, owing to the lack of scalable algorithms that exploit all aspects of available data - namely the directionality of flow of information and the dynamics thereof. Most existing methods use measures of connectedness in the graphical structure. In this paper, we present a fast, scalable algorithm to detect communities in directed, weighted graph representations of social networks by simulating flow of information through them. By design, our algorithm naturally handles undirected or unweighted networks as well. Our algorithmruns in O(|E|) time, which is better than most existing work and uses O(|E|) space and hence scales easily to very large datasets. Finally, we show that our algorithm outperforms the state-of-the-art Markov Clustering Algorithm (MCL) [22] in both accuracy and scalability on ground truth data (in a number of cases, we can find communities in graphs too large for MCL)."},{img:new URL("/assets/paper2-c3481f9a.png",self.location).href,des:"    Community detection is a classical problem in the field of graph mining. While most algorithms work on the entire graph, it is often interesting in practice to recover only the community containing some given set of seed nodes. In this paper, we propose a novel approach to this problem, using some low-dimensional embedding of the graph based on random walks starting from the seed nodes. From this embedding, we propose some simple yet efficient versions of the PageRank algorithm as well as a novel algorithm, called WalkSCAN, that is able to detect multiple communities, possibly overlapping. We provide insights into the performance of these algorithms through the theoretical analysis of a toy network and show that WalkSCAN outperforms existing algorithms on real networks."},{img:new URL("/assets/paper3-9034d6b1.png",self.location).href,des:"	  How can we detect communities when the social graphs is not available? We tackle this problem by modeling social contagion from a log of user activity, that is a dataset of tuples (u, i, t) recording the fact that user u “adopted” item i at time t. This is the only input to our problem.We propose a stochastic framework which assumes that item adoptions are governed by un underlying diffusion process over the unobserved social network, and that such diffusion model is based on community-level influence. By fitting the model parameters to the user activity log, we learn the community membership and the level of influence of each user in each community. This allows to identify for each community the “key” users, i.e., the leaders which are most likely to influence the rest of the community to adopt a certain item.The general framework can be instantiated with different diffusion models. In this paper we define two models: the extension to the community level of the classic (discrete time) Independent Cascade model, and a model that focuses on the time delay between adoptions.To the best of our knowledge, this is the first work studying community detection without the network."},{img:new URL("/assets/paper4-aa740db6.png",self.location).href,des:"    Community detection is an important task in network analysis. A community (also referred to as a cluster) is a set of cohesive vertices that have more connections inside the set than outside. In many social and information networks, these communities naturally overlap. For instance, in a social network, each vertex in a graph corresponds to an individual who usually participates in multiple communities. One of the most successful techniques for finding overlapping communities is based on local optimization and expansion of a community metric around a seed set of vertices. In this paper, we propose an efficient overlapping community detection algorithm using a seed set expansion approach. In particular, we develop new seeding strategies for a personalized PageRank scheme that optimizes the conductance community score. The key idea of our algorithm is to find good seeds, and then expand these seed sets using the personalized PageRank clustering procedure. Experimental results show that this seed set expansion approach outperforms other state-of-the-art overlapping community detection methods. We also show that our new seeding strategies are better than previous strategies, and are thus effective in finding good overlapping clusters in a graph."}],l=m=>{p.value.setActiveItem(m)},t=m=>{switch(m){case 0:s.value="4-1",o.push({path:"/visiual"});break}};return(m,v)=>{const y=ht,I=mt;return T(),M("div",vt,[d("div",gt,[d("div",yt,[wt,_t,bt,d("div",Ct,[d("button",{class:"btn1",onClick:v[0]||(v[0]=C=>t(0))},"开始使用"),d("button",{class:"btn2",onClick:v[1]||(v[1]=C=>t(1))},"了解更多")])]),It]),d("div",kt,[d("div",Et,[B(I,{height:"1000px",direction:"vertical",autoplay:!0,interval:1e4,onChange:l},{default:R(()=>[(T(),M(Y,null,Z(f,(C,g)=>B(y,{key:g},{default:R(()=>[d("img",{src:C.img,style:{height:"800px",width:"100%"}},null,8,Tt)]),_:2},1024)),64))]),_:1})]),d("div",Nt,[B(I,{height:"1000px",direction:"vertical",autoplay:!1,ref_key:"des",ref:p},{default:R(()=>[(T(),M(Y,null,Z(f,(C,g)=>B(y,{key:g},{default:R(()=>[St,d("div",Mt,ge(C.des),1)]),_:2},1024)),64))]),_:1},512)])])])}}},Ot=xe($t,[["__scopeId","data-v-3b3b7ff5"]]);export{Ot as default};
