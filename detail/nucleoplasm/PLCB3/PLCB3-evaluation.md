---
type: protein-evaluation
gene: "PLCB3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLCB3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLCB3 |
| 蛋白名称 | 1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase beta-3 |
| 蛋白大小 | 1234 aa / 138.8 kDa |
| UniProt ID | Q01970 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Cytoplasm; Membrane; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1234 aa / 138.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.3; PDB: 4GNK, 4QJ3, 4QJ4, 4QJ5, 7SQ2, 8EMV, 8EMW |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000008, IPR035892, IPR011992, IPR001192, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Supported |
| UniProt | Cytoplasm; Membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleus (GO:0005634)
- postsynaptic cytosol (GO:0099524)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 162 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Transcriptional profiling identification of inflammatory signaling pathways in ulcerative colitis.. *PloS one*. PMID: 40892863
2. OSBPL2 compound heterozygous variants cause dyschromatosis, ichthyosis, deafness and atopic disease syndrome.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 38701954
3. Multiple signals regulate phospholipase CBeta3 in human myometrial cells.. *Biology of reproduction*. PMID: 18322273
4. Cetuximab inhibits colorectal cancer development through inactivating the Wnt/β-catenin pathway and modulating PLCB3 expression.. *Scientific reports*. PMID: 38724565
5. Phospholipase Cβ3 mediates LH-induced granulosa cell differentiation.. *Endocrinology*. PMID: 21586561

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.3 |
| 高置信度残基 (pLDDT>90) 占比 | 62.2% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 79.9% |
| 可用 PDB 条目 | 4GNK, 4QJ3, 4QJ4, 4QJ5, 7SQ2, 8EMV, 8EMW, 8EMX, 8UQN, 8UQO |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4GNK, 4QJ3, 4QJ4, 4QJ5, 7SQ2, 8EMV, 8EMW, 8EMX, 8UQN, 8UQO）+ AlphaFold极高置信度预测（pLDDT=82.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR011992, IPR001192, IPR016280; Pfam: PF00168, PF17787, PF00388 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNAQ | 0.999 | 0.903 | — |
| ITPR1 | 0.968 | 0.071 | — |
| ITPR3 | 0.967 | 0.071 | — |
| GNA11 | 0.952 | 0.072 | — |
| GNB3 | 0.949 | 0.000 | — |
| GNA15 | 0.948 | 0.071 | — |
| GNA14 | 0.946 | 0.072 | — |
| PRKCA | 0.936 | 0.000 | — |
| GNAI3 | 0.935 | 0.067 | — |
| GNAI1 | 0.930 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257125 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19463016|imex:IM-17246 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |
| Ptpn6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-13607|pubmed:19647226 |
| EBI-1257121 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| Kif13b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SYNCRIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SORT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| NEDD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| KCNE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.3 + PDB: 4GNK, 4QJ3, 4QJ4, 4QJ5, 7SQ2,  | pLDDT=82.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Membrane; Nucleus / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLCB3 — 1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase beta-3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1234 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01970
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149782-PLCB3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLCB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01970
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
