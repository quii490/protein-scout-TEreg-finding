---
type: protein-evaluation
gene: "PLSCR4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLSCR4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLSCR4 |
| 蛋白名称 | Phospholipid scramblase 4 |
| 蛋白大小 | 329 aa / 37.0 kDa |
| UniProt ID | Q9NRQ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Cell membrane; Cell membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 329 aa / 37.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.4; PDB: 3Q5U |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005552; Pfam: PF03803 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Approved |
| UniProt | Cell membrane; Cell membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of M2 Macrophage-Related Key Genes in Advanced Atherosclerotic Plaques by Network-Based Analysis.. *Journal of cardiovascular pharmacology*. PMID: 38194604
2. Effect of Allergen-Specific Immunotherapy on Transcriptomic Changes in Canine Atopic Dermatitis.. *International journal of molecular sciences*. PMID: 37511372
3. MiR-103-5p deficiency suppresses lipid accumulation via upregulating PLSCR4 and its host gene PANK3 in goat mammary epithelial cells.. *International journal of biological macromolecules*. PMID: 38583827
4. Biomarkers and potential function analysis of triple-negative breast cancer screening based on bioinformatics.. *Cancer biomarkers : section A of Disease markers*. PMID: 40179432
5. Whole blood transcriptomic analysis reveals PLSCR4 as a potential marker for vaso-occlusive crises in sickle cell disease.. *Scientific reports*. PMID: 34772994

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.4 |
| 高置信度残基 (pLDDT>90) 占比 | 37.1% |
| 置信残基 (pLDDT 70-90) 占比 | 18.8% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 30.1% |
| 有序区域 (pLDDT>70) 占比 | 55.9% |
| 可用 PDB 条目 | 3Q5U |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.4），有序残基占 55.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005552; Pfam: PF03803 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KRTAP6-1 | 0.591 | 0.591 | — |
| TRIP13 | 0.574 | 0.574 | — |
| CD4 | 0.567 | 0.000 | — |
| FBLN1 | 0.496 | 0.433 | — |
| ZDHHC17 | 0.445 | 0.422 | — |
| PLSCR1 | 0.433 | 0.307 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EFEMP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Hoxa1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15418|pubmed:23088713 |
| Q81YS3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| MRGBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| RUVBL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| RUVBL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| PDCD6 | psi-mi:"MI:0096"(pull down) | pubmed:18256029|imex:IM-19024 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 15
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.4 + PDB: 3Q5U | pLDDT=69.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell membrane; Nucleus / Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 6 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLSCR4 — Phospholipid scramblase 4，非常新颖，仅有少数基础研究。
2. 蛋白大小329 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRQ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114698-PLSCR4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLSCR4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRQ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
