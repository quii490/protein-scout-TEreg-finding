---
type: protein-evaluation
gene: "NCOR1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NCOR1 — REJECTED (研究热度过高 (PubMed strict=317，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCOR1 / KIAA1047 |
| 蛋白名称 | Nuclear receptor corepressor 1 |
| 蛋白大小 | 2440 aa / 270.2 kDa |
| UniProt ID | O75376 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2440 aa / 270.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=317 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=40.7; PDB: 2EQR, 3H52, 3KMZ, 3N00, 4MDD, 4WVD, 6ONI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009057, IPR017930, IPR051571, IPR031557, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- histone deacetylase complex (GO:0000118)
- membrane (GO:0016020)
- mitotic spindle (GO:0072686)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 317 |
| PubMed broad count | 854 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1047 |

**关键文献**:
1. Therapeutic regulation of autophagy in hepatic metabolism.. *Acta pharmaceutica Sinica. B*. PMID: 35127371
2. De novo genic mutations among a Chinese autism spectrum disorder cohort.. *Nature communications*. PMID: 27824329
3. The transcriptional landscape of Shh medulloblastoma.. *Nature communications*. PMID: 33741928
4. Ubiquitin ligase RNF20 coordinates sequential adipose thermogenesis with brown and beige fat-specific substrates.. *Nature communications*. PMID: 38296968
5. Insights into the function of HDAC3 and NCoR1/NCoR2 co-repressor complex in metabolic diseases.. *Frontiers in molecular biosciences*. PMID: 37674539

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 40.7 |
| 高置信度残基 (pLDDT>90) 占比 | 3.6% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 81.5% |
| 有序区域 (pLDDT>70) 占比 | 12.3% |
| 可用 PDB 条目 | 2EQR, 3H52, 3KMZ, 3N00, 4MDD, 4WVD, 6ONI, 6WMQ, 6WMS, 6XXS |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=40.7），有序残基占 12.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009057, IPR017930, IPR051571, IPR031557, IPR001005; Pfam: PF15784, PF00249 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPARG | 0.999 | 0.984 | — |
| GPS2 | 0.999 | 0.780 | — |
| BCL6 | 0.999 | 0.979 | — |
| NR1D1 | 0.999 | 0.811 | — |
| RARA | 0.999 | 0.988 | — |
| TBL1X | 0.999 | 0.902 | — |
| TBL1XR1 | 0.999 | 0.915 | — |
| HDAC4 | 0.999 | 0.828 | — |
| HDAC1 | 0.999 | 0.435 | — |
| HDAC3 | 0.999 | 0.933 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q60812 | psi-mi:"MI:0096"(pull down) | pubmed:12904255|imex:IM-26835 |
| NELFE | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| Dach1 | psi-mi:"MI:0096"(pull down) | pubmed:12130660 |
| Dach2 | psi-mi:"MI:0096"(pull down) | pubmed:12130660 |
| Sap30 | psi-mi:"MI:0096"(pull down) | pubmed:9702189 |
| Sin3a | psi-mi:"MI:0096"(pull down) | pubmed:9702189 |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| RARA | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TULP3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=40.7 + PDB: 2EQR, 3H52, 3KMZ, 3N00, 4MDD,  | pLDDT=40.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. NCOR1 — Nuclear receptor corepressor 1，研究基础较多，新颖性有限。
2. 蛋白大小2440 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 317 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=40.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 317 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75376
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141027-NCOR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCOR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75376
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
