---
type: protein-evaluation
gene: "FBXW4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXW4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXW4 / FBW4, SHFM3 |
| 蛋白名称 | F-box/WD repeat-containing protein 4 |
| 蛋白大小 | 412 aa / 46.3 kDa |
| UniProt ID | P57775 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 412 aa / 46.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR052301, IPR015943, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- SCF ubiquitin ligase complex (GO:0019005)
- ubiquitin ligase complex (GO:0000151)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 57 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBW4, SHFM3 |

**关键文献**:
1. Pivotal Role of FBXW4 in Glioma Progression and Prognosis.. *Genetics research*. PMID: 39377096
2. Elucidating the role of FBXW4 in osteoporosis: integrating bioinformatics and machine learning for advanced insight.. *BMC pharmacology & toxicology*. PMID: 39881357
3. FBXW4 Is Highly Expressed and Associated With Poor Survival in Acute Myeloid Leukemia.. *Frontiers in oncology*. PMID: 32175272
4. Identification of hypertrophy-modulating Cullin-RING ubiquitin ligases in primary cardiomyocytes.. *Frontiers in physiology*. PMID: 36969608
5. The novel ubiquitin ligase complex, SCF(Fbxw4), interacts with the COP9 signalosome in an F-box dependent manner, is mutated, lost and under-expressed in human cancers.. *PloS one*. PMID: 23658844

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.5 |
| 高置信度残基 (pLDDT>90) 占比 | 77.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 4.1% |
| 有序区域 (pLDDT>70) 占比 | 92.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.5，有序区 92.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR052301, IPR015943, IPR036322; Pfam: PF12937, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.933 | 0.782 | — |
| POLL | 0.925 | 0.000 | — |
| CUL1 | 0.911 | 0.818 | — |
| LBX1 | 0.894 | 0.000 | — |
| CCT5 | 0.885 | 0.775 | — |
| CCT3 | 0.863 | 0.730 | — |
| CCT4 | 0.861 | 0.676 | — |
| CCT8 | 0.859 | 0.730 | — |
| CCT7 | 0.843 | 0.692 | — |
| TXNDC9 | 0.819 | 0.814 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLX4IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| CDC37 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |
| ECSIT | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |
| MAST1 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |
| RNF32 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |
| COPS6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22632967|imex:IM-17368 |
| CCT6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDCL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.5 + PDB: 无 | pLDDT=90.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FBXW4 — F-box/WD repeat-containing protein 4，非常新颖，仅有少数基础研究。
2. 蛋白大小412 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 深度机制分析

**F-box/WD40双重结构域的泛素连接酶适配架构**：FBXW4（412 aa, 46.3 kDa, UniProt P57775）是SCF（SKP1-CUL1-F-box）E3泛素连接酶复合物的F-box适配亚基——N端约40 aa的F-box基序（IPR001810, Pfam:PF12937, aa 3-35）识别并锚定于SKP1-CUL1-RBX1 E3核心支架，C端约360 aa由7个WD40 β-propeller叶片组成（IPR015943, IPR036322, Pfam:PF00400），以7叶螺旋桨折叠提供底物蛋白识别表面。WD40叶片间的可变环区决定底物选择性——FBXW4属Fbw亚家族（WD40型F-box蛋白），与FBXW7（经典肿瘤抑制因子，识别磷酸化degron）共享域架构但底物偏好不同。AlphaFold pLDDT=90.5（77.9%>90, 92.9%有序）确认全蛋白的高质量折叠——F-box基序可能采用α-螺旋构象嵌入SKP1的C端凹槽，而WD40域的7叶β-propeller以高刚性维持底物识别口袋。

**SCF E3复合物组装与CCT/伴侣蛋白的折叠质量控制**：STRING互作数据完美再现SCF核心复合物：SKP1（combined score=0.933, 实验=0.782）为衔接蛋白桥接F-box与CUL1；CUL1（0.911, 实验=0.818）为cullin支架蛋白，其N端结合SKP1、C端招募RBX1-泛素偶联酶（E2），构成完整泛素转移级联。IntAct实验验证了SKP1的共免疫沉淀（PMID:22632967）和COPS6/CSN6的串联纯化（PMID:21145461）——COPS6是COP9信号体（CSN）的亚基，CSN通过CUL1的去neddylation动态调控SCF复合物组装。最为独特的是CCT/TRiC伴侣蛋白系统的全面互作：CCT5（0.885, 实验=0.775）、CCT3（0.863, 实验=0.730）、CCT4（0.861, 实验=0.676）、CCT8（0.859, 实验=0.730）、CCT7（0.843, 实验=0.692）——双环型ATP驱动的蛋白折叠室——与FBXW4的极高置信互作（全部有实验证据）暗示CCT/TRiC可能是FBXW4 WD40域的专属折叠伴侣。TXNDC9（0.819, 实验=0.814）是硫氧还蛋白域含蛋白，参与氧化还原调控的蛋白折叠——在氧化应激条件下可能调节FBXW4的底物识别构象。

**高尔基体定位的SCF E3与非核功能特征**：FBXW4的HPA可靠定位为Golgi apparatus（Approved），GO-CC列出SCF ubiquitin ligase complex（GO:0019005）和ubiquitin ligase complex（GO:0000151），但无任何核定位注释（UniProt亦无）。这一细胞区室定位强烈暗示FBXW4的底物识别和泛素化功能完全在高尔基体/内质网-高尔基中间区室（ERGIC）中执行——可能靶向高尔基体驻留蛋白的降解以维持高尔基体结构完整性和膜运输。SLX4IP（IntAct co-IP, PMID:19596235）为端粒替代延长（ALT）通路蛋白——若此互作在高尔基体发生，暗示FBXW4参与端粒维持的膜相关机制。

**TE调控——不推荐**：FBXW4因核定位证据极弱（2/10, 8/40分）已被REJECTED标签拒绝。WD40域虽理论上可进化出DNA/RNA结合表面，但目前无证据显示FBXW4的WD40域结合核酸。SCF E3对TE沉默的贡献通常通过核内F-box蛋白实现——如FBXO44直接识别H3K9me2标记促进TE抑制。FBXW4定位于高尔基体并缺乏任何核区室注释，使其参与TE调控的可能性可忽略。尽管如此，其极高结构质量（pLDDT=90.5）和完善的PPI网络使FBXW4成为研究SCF-CCT/TRiC组装和WD40底物识别的优秀生化和结构生物学模型。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P57775
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107829-FBXW4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXW4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P57775
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000107829-FBXW4/subcellular

![](https://images.proteinatlas.org/43496/481_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43496/481_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43496/487_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43496/487_A12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P57775-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
