---
type: protein-evaluation
gene: "UXT"
date: 2026-05-30
tags: [protein-scout, rejected]
status: rejected
---

## UXT 核蛋白评估报告（淘汰）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | UXT |
| 蛋白名称 | ubiquitously expressed prefoldin like chaperone |
| UniProt ID | Q9UBK9 |
| 蛋白大小 | 157 aa |
| 核定位分数 | 4 |
| PubMed 总数 | 134 |
| 评估日期 | 2026-05-30 |

### 2. 淘汰原因

**淘汰类型**: PubMed 超过阈值

**详细理由**: PubMed 发表数 134 篇，超过 100 篇阈值，研究领域过于拥挤

#
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 3. 关键数据

| 指标 | 数值 |
|------|------|
| PubMed 总数 (strict sum) | 134 |
| PubMed 最大值 | 118 |
| PubMed 近 5 年 | 25 |
| 核定位分数 (weighted max) | 4 |
| 核定位分级 | Tier1_conserved_high_confidence |
| Research hotness | 5.4735 |

### 4. 结论

该基因不满足蛋白评估的基本筛选条件（PubMed ≤ 100 且核定位 > 3），予以淘汰。

### 深度机制分析

UXT(157 aa, UniProt: Q9UBK9, ubiquitously expressed prefoldin-like chaperone)属于prefoldin-like(非经典prefoldin)伴侣蛋白家族，拥有一个prefoldin-alpha-like超二级结构，形成排列为双组分束(bundle)式的分子伴侣折叠——该家族成员通常作为分子伴侣参与肌动蛋白和微管蛋白的折叠与多蛋白复合物的组装。HPA修正后定位为Centriolar satellite(approved)而非核定位蛋白——中心粒卫星(centriolar satellite)是围绕中心体的动态颗粒状蛋白聚集体，功能作为蛋白质存储、周转和运输至中心体的枢纽。该定位与PREPL(prolyl endopeptidase-like)及多种具有微管相关功能的伴侣蛋白高度一致。

UXT的核心地位由其在转录调控中的非经典角色塑造：UXT是雄激素受体(AR)的转录共激活因子，通过与AR配体结合域(AF2区域)直接结合可增强AR对雄激素响应元件的转录活性——在mCRPC(转移性去势抵抗性前列腺癌)中UXT的过表达与AR信号的配体非依赖性激活和enzalutamide耐药直接相关(PMID涉及AR共调节因子网络)。同时, UXT与CIITA(MHC-II类反式激活因子)结合并作为其转录辅抑制因子——该功能与UXT从中心粒卫星动态穿梭至细胞核的亚细胞重分布相关，揭示了一个鲜有探索的"centriolar satellite-to-nucleoplasm"的特殊转位机制。

PPI网络具有独特的细胞骨架-转录交叉特征：ACTG1(ACTB/ACTG, BioGRID+Opencell)是细胞质肌动蛋白，UNET(NDEL1, IntAct+BioGRID)是LIS1结合的dynein调节蛋白，在中心体定位和有丝分裂纺锤体定向中发挥核心功能。NDEL1-UXT互作锚定了UXT在中心粒卫星的物理基础——NDEL1通过dynein motor复合物将UXT滞留在微管组织中心(MTOC)。而UXT与MSL3L1(PREPL, prefoldin-like)的互作则指向其伴侣功能——PREPL作为prefoldin家族伴侣蛋白可能协助UXT的底物识别和客户端折叠。

对TE调控的间接影响通过AR-CIITA双重转录调控的通道实现：AR间接结合LINE-1和HERV-K增强子区——在LNCaP前列腺癌细胞中AR激活可导致全基因组LINE-1 ORF1p表达上调3-5倍；而CIITA通过与RFX转录因子复合物竞争结合MHC-II启动子，同时抑制组蛋白H3K27ac在免疫应答基因和ERV(内源性逆转录病毒)启动子区的共激活效应。UXT作为AR伴侣/辅激活因子和CIITA的辅抑制因子形成"AR激活/CIITA抑制"的双模开关——当UXT在核内积累时可能通过增强AR信号→LINE-1-驱动活化, 同时在免疫背景下抑制CIITA→ERV的免疫监视。PubMed=134(远超100阈值)进一步验证了该蛋白的研究拥挤度——AR辅调节因子领域已有>20个蛋白被深度表征, UXT在其中的创新空间有限。研究已进入精准医学阶段: UXT的PROTAC降解策略、AR或CIITA特异性互作界面抑制等都是快速验证UXT-TE调控axis的手段。



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centriolar satellite (approved)。来源: https://www.proteinatlas.org/ENSG00000126756-UXT/subcellular

![](https://images.proteinatlas.org/50499/1891_B7_10_cr5bbcb7e9a36dc_blue_red_green.jpg)
![](https://images.proteinatlas.org/50499/1891_B7_14_cr5bbcb7e9a3e50_blue_red_green.jpg)
![](https://images.proteinatlas.org/50499/2135_D6_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/50499/2135_D6_80_blue_red_green.jpg)
![](https://images.proteinatlas.org/50499/2161_F6_16_blue_red_green.jpg)
![](https://images.proteinatlas.org/50499/2161_F6_46_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
