---
type: protein-evaluation
gene: "JUNB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## JUNB — REJECTED (研究热度过高 (PubMed strict=1842，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JUNB |
| 蛋白名称 | Transcription factor JunB |
| 蛋白大小 | 347 aa / 35.9 kDa |
| UniProt ID | P17275 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 347 aa / 35.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1842 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050946, IPR004827, IPR046347, IPR005643, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)
- transcription factor AP-1 complex (GO:0035976)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1842 |
| PubMed broad count | 2388 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. NAT10/ac4C/JunB facilitates TNBC malignant progression and immunosuppression by driving glycolysis addiction.. *Journal of experimental & clinical cancer research : CR*. PMID: 39363363
2. MEK inhibition prevents CAR-T cell exhaustion and differentiation via downregulation of c-Fos and JunB.. *Signal transduction and targeted therapy*. PMID: 39438476
3. Circadian control of ConA-induced acute liver injury and inflammatory response via Bmal1 regulation of Junb.. *JHEP reports : innovation in hepatology*. PMID: 37791375
4. LDHA promotes osteoblast differentiation through histone lactylation.. *Biochemical and biophysical research communications*. PMID: 35605402
5. JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40549917

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.5 |
| 高置信度残基 (pLDDT>90) 占比 | 20.2% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 21.9% |
| 低置信 (pLDDT<50) 占比 | 50.4% |
| 有序区域 (pLDDT>70) 占比 | 27.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.5），有序残基占 27.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050946, IPR004827, IPR046347, IPR005643, IPR002112; Pfam: PF00170, PF03957 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JUN | 0.999 | 0.639 | — |
| FOSL1 | 0.999 | 0.830 | — |
| FOSB | 0.999 | 0.728 | — |
| JUND | 0.999 | 0.704 | — |
| FOSL2 | 0.999 | 0.880 | — |
| FOS | 0.999 | 0.907 | — |
| BATF | 0.997 | 0.937 | — |
| MAPK9 | 0.979 | 0.701 | — |
| MAPK8 | 0.973 | 0.568 | — |
| EGR1 | 0.970 | 0.634 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NINL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FOSL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BATF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| ATF4 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| TDG | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| BDNF | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HOXA7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NEU1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MAPK6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SET | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.5 + PDB: 无 | pLDDT=59.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. JUNB — Transcription factor JunB，研究基础较多，新颖性有限。
2. 蛋白大小347 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1842 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1842 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17275
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171223-JUNB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JUNB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17275
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000171223-JUNB/subcellular

![](https://images.proteinatlas.org/19149/2269_D2_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/19149/2269_D2_60_blue_red_green.jpg)
![](https://images.proteinatlas.org/19149/115_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/19149/115_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/19149/116_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/19149/116_D3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P17275-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
