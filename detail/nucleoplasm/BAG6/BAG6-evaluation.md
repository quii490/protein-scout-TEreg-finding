---
type: protein-evaluation
gene: "BAG6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BAG6 — REJECTED (研究热度过高 (PubMed strict=152，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BAG6 / BAT3, G3 |
| 蛋白名称 | Large proline-rich protein BAG6 |
| 蛋白大小 | 1132 aa / 119.4 kDa |
| UniProt ID | P46379 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Cytoplasm, cytosol; Nucleus; Secreted, extracellular exosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 1132 aa / 119.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=152 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.6; PDB: 1WX9, 2N9P, 4DWF, 4EEW, 4WWR, 4X86, 6AU8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR021925, IPR048926, IPR000626, IPR029071, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Supported |
| UniProt | Cytoplasm, cytosol; Nucleus; Secreted, extracellular exosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- BAT3 complex (GO:0071818)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 152 |
| PubMed broad count | 256 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BAT3, G3 |

**关键文献**:
1. Noncoding translation mitigation.. *Nature*. PMID: 37046090
2. Mechanisms of readthrough mitigation reveal principles of GCN1-mediated translational quality control.. *Cell*. PMID: 37339632
3. Genetic Influence of the Brain on Muscle Structure: A Mendelian Randomization Study of Sarcopenia.. *Journal of cachexia, sarcopenia and muscle*. PMID: 39535371
4. C9orf72 protein quality control by UBR5-mediated heterotypic ubiquitin chains.. *EMBO reports*. PMID: 37317656
5. Molecular determinants of the crosstalk between endosomal microautophagy and chaperone-mediated autophagy.. *Cell reports*. PMID: 38060380

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.6 |
| 高置信度残基 (pLDDT>90) 占比 | 17.3% |
| 置信残基 (pLDDT 70-90) 占比 | 23.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 52.3% |
| 有序区域 (pLDDT>70) 占比 | 41.2% |
| 可用 PDB 条目 | 1WX9, 2N9P, 4DWF, 4EEW, 4WWR, 4X86, 6AU8, 7RU9, 7RUA, 7RUC |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.6），有序残基占 41.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021925, IPR048926, IPR000626, IPR029071, IPR019954; Pfam: PF12057, PF20960, PF00240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBL4A | 0.999 | 0.991 | — |
| GET4 | 0.999 | 0.991 | — |
| RNF126 | 0.997 | 0.991 | — |
| FAF2 | 0.995 | 0.994 | — |
| UBXN1 | 0.995 | 0.994 | — |
| NCR3 | 0.995 | 0.781 | — |
| DESI1 | 0.994 | 0.994 | — |
| SGTA | 0.993 | 0.874 | — |
| GET3 | 0.978 | 0.787 | — |
| HAVCR2 | 0.941 | 0.345 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000397894.2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18055229|imex:IM-25760 |
| ENSP00000413698.2 | psi-mi:"MI:0071"(molecular sieving) | imex:IM-25773|pubmed:24133212 |
| Gnai3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Traf6 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Camk2a | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Tnfrsf11a | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| KLHL12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EFEMP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SGTA | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| UBL7 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.6 + PDB: 1WX9, 2N9P, 4DWF, 4EEW, 4WWR,  | pLDDT=56.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus; Secreted, extracellul / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BAG6 — Large proline-rich protein BAG6，研究基础较多，新颖性有限。
2. 蛋白大小1132 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 152 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 152 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P46379
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204463-BAG6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BAG6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46379
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
