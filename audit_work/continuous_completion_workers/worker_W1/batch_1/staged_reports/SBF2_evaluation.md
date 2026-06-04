---
type: protein-evaluation
gene: "SBF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SBF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SBF2 / CMT4B2, KIAA1766, MTMR13 |
| 蛋白名称 | Myotubularin-related protein 13 |
| 蛋白大小 | 1849 aa / 208.5 kDa |
| UniProt ID | Q86WG5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Intermediate filaments, Cytosol; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Membrane; Endosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1849 aa / 208.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=69 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001194, IPR005112, IPR043153, IPR004182, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Intermediate filaments, Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Membrane; Endosome membrane; Cell projection, axon | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- membrane (GO:0016020)
- perinuclear region of cytoplasm (GO:0048471)
- vacuolar membrane (GO:0005774)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 69 |
| PubMed broad count | 152 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CMT4B2, KIAA1766, MTMR13 |

**关键文献**:
1. Charcot-Marie-Tooth Hereditary Neuropathy Overview.. **. PMID: 20301532
2. Novel SBF2 mutations and clinical spectrum of Charcot-Marie-Tooth neuropathy type 4B2.. *Clinical genetics*. PMID: 30028002
3. Long Noncoding RNASBF2-AS1 Promotes Gastric Cancer Progression via Regulating miR-545/EMS1 Axis.. *BioMed research international*. PMID: 32626753
4. YBX1/lncRNA SBF2-AS1 interaction regulates proliferation and tamoxifen sensitivity via PI3K/AKT/MTOR signaling in breast cancer cells.. *Molecular biology reports*. PMID: 36754932
5. siRNA-Mediated SBF2 Silencing May Inhibit Pancreatic Cancer Cells via Attenuation of the TGF-β Signaling Pathway.. *Technology in cancer research & treatment*. PMID: 25882882

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.2 |
| 高置信度残基 (pLDDT>90) 占比 | 25.6% |
| 置信残基 (pLDDT 70-90) 占比 | 43.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 20.7% |
| 有序区域 (pLDDT>70) 占比 | 68.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.2，有序区 68.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001194, IPR005112, IPR043153, IPR004182, IPR037823; Pfam: PF02141, PF02893, PF06602 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTMR2 | 0.991 | 0.686 | — |
| RAB21 | 0.816 | 0.136 | — |
| SH3TC2 | 0.788 | 0.000 | — |
| FGD4 | 0.786 | 0.000 | — |
| MTMR1 | 0.765 | 0.675 | — |
| FIG4 | 0.741 | 0.000 | — |
| GDAP1 | 0.741 | 0.000 | — |
| ADGRD1 | 0.719 | 0.000 | — |
| ADGRG6 | 0.714 | 0.000 | — |
| NPR3 | 0.673 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| FOS | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| HNRNPU | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| FHL3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RBPMS | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| HNRNPD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SYNCRIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| BAG6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.2 + PDB: 无 | pLDDT=73.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Membrane / Nucleoplasm; 额外: Intermediate filaments, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SBF2 — Myotubularin-related protein 13，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1849 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 69 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86WG5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133812-SBF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SBF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86WG5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
