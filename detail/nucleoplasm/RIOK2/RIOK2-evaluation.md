---
type: protein-evaluation
gene: "RIOK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RIOK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RIOK2 / RIO2 |
| 蛋白名称 | Serine/threonine-protein kinase RIO2 |
| 蛋白大小 | 552 aa / 63.3 kDa |
| UniProt ID | Q9BVS4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Plasma membrane; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 552 aa / 63.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.4; PDB: 5DHF, 6FDM, 6FDN, 6FDO, 6G18, 6G51, 6HK6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR030484, IPR015285, IPR018934, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Plasma membrane | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- preribosome, small subunit precursor (GO:0030688)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RIO2 |

**关键文献**:
1. RIO-kinase 2 is essential for hematopoiesis.. *PloS one*. PMID: 38564577
2. RIOK2 kinase regulates the translocation of the FADD-RIPK1-Caspase-8 complex to the ER and the cleavage of Gasdermin D to drive pyroptosis.. *Nature communications*. PMID: 41249793
3. Phospholipase PLCE1 Promotes Transcription and Phosphorylation of MCM7 to Drive Tumor Progression in Esophageal Cancer.. *Cancer research*. PMID: 38117512
4. RIOK2 Contributes to Cell Growth and Protein Synthesis in Human Oral Squamous Cell Carcinoma.. *Current oncology (Toronto, Ont.)*. PMID: 36661680
5. Blockade of IL-22 signaling reverses erythroid dysfunction in stress-induced anemias.. *Nature immunology*. PMID: 33753942

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.4 |
| 高置信度残基 (pLDDT>90) 占比 | 31.2% |
| 置信残基 (pLDDT 70-90) 占比 | 25.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 34.4% |
| 有序区域 (pLDDT>70) 占比 | 56.7% |
| 可用 PDB 条目 | 5DHF, 6FDM, 6FDN, 6FDO, 6G18, 6G51, 6HK6, 7VBT, 7WU0, 9F81 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.4），有序残基占 56.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR030484, IPR015285, IPR018934, IPR000687; Pfam: PF01163, PF09202 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSR1 | 0.999 | 0.997 | — |
| LTV1 | 0.999 | 0.997 | — |
| NOB1 | 0.999 | 0.993 | — |
| RPS2 | 0.999 | 0.994 | — |
| BYSL | 0.999 | 0.991 | — |
| RPS15 | 0.997 | 0.994 | — |
| RPS5 | 0.997 | 0.994 | — |
| RPS3 | 0.996 | 0.991 | — |
| PNO1 | 0.996 | 0.955 | — |
| KRR1 | 0.996 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| RPRD1A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SMAD3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RELA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GFUS | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| EIF3L | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| G3BP1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| EWSR1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| EIF3B | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.4 + PDB: 5DHF, 6FDM, 6FDN, 6FDO, 6G18,  | pLDDT=67.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RIOK2 — Serine/threonine-protein kinase RIO2，非常新颖，仅有少数基础研究。
2. 蛋白大小552 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BVS4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000058729-RIOK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RIOK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BVS4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
