---
type: protein-evaluation
gene: "HIF1A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HIF1A — REJECTED (研究热度过高 (PubMed strict=2244，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HIF1A |
| 蛋白名称 | HIF1A (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | HIF1A |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2244 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Enhanced |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2244 |
| PubMed broad count | 15000 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. HIF1A Alleviates compression-induced apoptosis of nucleus pulposus derived stem cells via upregulating autophagy.. *Autophagy*. PMID: 33455530
2. USP21 deubiquitinates and stabilizes HSP90 and ENO1 to promote aerobic glycolysis and proliferation in cholangiocarcinoma.. *International journal of biological sciences*. PMID: 38385089
3. Single-Cell RNA Sequencing to Dissect the Immunological Network of Autoimmune Myocarditis.. *Circulation*. PMID: 32431172
4. Hypoxia-induced BNIP3 facilitates the progression and metastasis of uveal melanoma by driving metabolic reprogramming.. *Autophagy*. PMID: 39265983
5. USP51 facilitates colorectal cancer stemness and chemoresistance by forming a positive feed-forward loop with HIF1A.. *Cell death and differentiation*. PMID: 37816999

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EGLN3 | 0.999 | 0.942 | — |
| ARNT | 0.999 | 0.999 | — |
| CUL2 | 0.999 | 0.788 | — |
| CREBBP | 0.999 | 0.991 | — |
| HIF1AN | 0.999 | 0.991 | — |
| ARNT2 | 0.999 | 0.694 | — |
| EGLN2 | 0.999 | 0.892 | — |
| TP53 | 0.999 | 0.847 | — |
| EP300 | 0.999 | 0.999 | — |
| ELOB | 0.999 | 0.966 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RWDD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11867|pubmed:17956732 |
| ENSP00000338018.4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| SSX4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EP300 | psi-mi:"MI:0096"(pull down) | pubmed:15261140 |
| Prkce | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11139474 |
| Arnt | psi-mi:"MI:0413"(electrophoretic mobility shift as | pubmed:10873592|imex:IM-20084 |
| Arnt2 | psi-mi:"MI:0413"(electrophoretic mobility shift as | pubmed:10873592|imex:IM-20084 |
| KAT2B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14472|pubmed:16543236 |
| HIF1AN | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12446723 |
| OS9 | psi-mi:"MI:0018"(two hybrid) | pubmed:15721254|imex:IM-19692 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm, Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HIF1A — HIF1A (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2244 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2244 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/HIF1A
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100644-HIF1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HIF1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/HIF1A
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000100644-HIF1A/subcellular

![](https://images.proteinatlas.org/907/1653_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/907/1653_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/907/1703_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/907/1703_C1_8_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
