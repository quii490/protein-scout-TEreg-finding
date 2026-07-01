---
type: protein-evaluation
gene: "KLK7"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, rejected]
status: rejected
---

## KLK7 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KLK7 |
| 蛋白大小 | 253 aa / 27.5 kDa |
| UniProt ID | P49862 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nuclear membrane; Plasma membrane (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 253 aa |
| 新颖性 | 0/10 | ×5 | 0.0 | PubMed=161 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=91.6; PDB=12 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Peptidase_S1_PA; Peptidase_S1_PA_chymotrypsin; Peptidase_S1A |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=84 |
| **加权总分** | | | **95/180** | |
| **归一化总分** | | | **53.0/100** | 互证: +2 |

### 3. 分析
- Nuclear membrane; Plasma membrane (Supported)
- PubMed strict=161 broad=360
- AF pLDDT=91.6 PDB=12
- InterPro: Peptidase_S1_PA; Peptidase_S1_PA_chymotrypsin; Peptidase_S1A
- Pfam: Trypsin
- PPI degree=84 ChIP: None
36516271: Dual antibody inhibition of KLK5 and KLK7 for Netherton syndrome and atopic derm | 38124525: A pharmacogenetic study of psoriasis supports the association between a gene (KL | 40154838: The serine protease KLK7 promotes immune cell infiltration in visceral adipose t

### 深度机制分析

KLK7（UniProt P49862）属于组织激肽释放酶（tissue kallikrein）丝氨酸蛋白酶家族，其催化结构域采用经典的胰蛋白酶样丝氨酸蛋白酶折叠（trypsin-like serine protease fold, Peptidase_S1_PA/PF00089）——由两个6链beta桶组成的双结构域架构，催化三联体His57-Asp102-Ser195（胰蛋白酶编号）位于domain界面裂缝中，执行肽键水解。KLK7具有糜蛋白酶样（chymotrypsin-like）底物特异性，偏好切割P1位为Tyr/Phe的肽键，这与KLK5（胰蛋白酶样，偏好Arg/Lys）形成功能互补。AlphaFold v6预测pLDDT高达91.6，12个PDB实验结构（包含apo形式和多种抑制剂复合物）已完整解析其活性位点构象、底物识别模式和别构调控机制，结构可信度在所有丝氨酸蛋白酶中位列前茅。

KLK7的生理功能集中在表皮屏障稳态：在表皮颗粒层和角质层中分泌表达，通过切割桥粒芯蛋白desmoglein 1和corneodesmosin，促进角质细胞的程序性脱落（desquamation）。这一功能使KLK7成为Netherton综合征和特应性皮炎的核心致病因子——KLK7和KLK5的双重抗体抑制策略已被开发为Netherton综合征的治疗方案（PMID:36516271）。PPI网络达到84个互作伙伴，反映了作为分泌型蛋白酶在胞外基质中的广泛底物谱。

HPA IF检测到KLK7定位于Nuclear membrane和Plasma membrane（Supported），这一非典型定位值得审视。胰蛋白酶家族丝氨酸蛋白酶通常通过信号肽进入分泌途径并在胞外空间中发挥功能，核膜定位极为罕见。可能的解释包括：（1）抗体非特异性结合导致假阳性信号；（2）KLK7的某些剪接变异体或翻译后修饰形式保留了内质网/核膜定位信号；（3）KLK7作为分泌蛋白在高尔基体/内质网中的合成过程导致核周膜染色。GO-CC注释集中于extracellular space/extracellular region，支持KLK7主要作为胞外蛋白酶的功能范式。

PubMed文献数161篇（broad=360）超过新颖性阈值，12个PDB结构提供了高分辨率的结构信息，但KLK7的功能范式（表皮脱屑/胞外蛋白酶）与TE调控的分子机制（核定位、染色质结合、核酸互作）之间不存在合理的功能连接。虽然丝氨酸蛋白酶的催化机制和抑制剂设计为药物化学提供了丰富的化学探针工具箱，但将KLK7作为TE调控候选蛋白缺乏最基础的功能前提——表皮特异性分泌蛋白不可能直接参与基因组TE的转录调控或表观遗传沉默。

### 4. 总体评价
**53.0/100** | **rejected**
Nuclear protein
