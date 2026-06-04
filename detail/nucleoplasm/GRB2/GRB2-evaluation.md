---
type: protein-evaluation
gene: "GRB2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GRB2 — REJECTED (研究热度过高 (PubMed strict=2898，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GRB2 / ASH |
| 蛋白名称 | Growth factor receptor-bound protein 2 |
| 蛋白大小 | 217 aa / 25.2 kDa |
| UniProt ID | P62993 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Centrosome; UniProt: Nucleus; Cytoplasm; Endosome; Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 217 aa / 25.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2898 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.7; PDB: 1AZE, 1BM2, 1BMB, 1CJ1, 1FHS, 1FYR, 1GCQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043539, IPR035643, IPR035641, IPR000980, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Centrosome | Supported |
| UniProt | Nucleus; Cytoplasm; Endosome; Golgi apparatus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cell-cell junction (GO:0005911)
- centrosome (GO:0005813)
- COP9 signalosome (GO:0008180)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endosome (GO:0005768)
- extracellular exosome (GO:0070062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2898 |
| PubMed broad count | 3893 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ASH |

**关键文献**:
1. GRB2 regulation of essential signaling pathways in the endometrium is critical for implantation and decidualization.. *Nature communications*. PMID: 40038241
2. Ginsenoside Rg3 Restores Mitochondrial Cardiolipin Homeostasis via GRB2 to Prevent Parkinson's Disease.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39159293
3. The Configuration of GRB2 in Protein Interaction and Signal Transduction.. *Biomolecules*. PMID: 38540680
4. GRB2 stabilizes RAD51 at reversed replication forks suppressing genomic instability and innate immunity against cancer.. *Nature communications*. PMID: 38459011
5. The Role of Grb2 in Cancer and Peptides as Grb2 Antagonists.. *Protein and peptide letters*. PMID: 29173143

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.7 |
| 高置信度残基 (pLDDT>90) 占比 | 67.3% |
| 置信残基 (pLDDT 70-90) 占比 | 26.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 2.8% |
| 有序区域 (pLDDT>70) 占比 | 93.6% |
| 可用 PDB 条目 | 1AZE, 1BM2, 1BMB, 1CJ1, 1FHS, 1FYR, 1GCQ, 1GFC, 1GFD, 1GHU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1AZE, 1BM2, 1BMB, 1CJ1, 1FHS, 1FYR, 1GCQ, 1GFC, 1GFD, 1GHU）+ AlphaFold极高置信度预测（pLDDT=88.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043539, IPR035643, IPR035641, IPR000980, IPR036860; Pfam: PF00017, PF00018 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERBB4 | 0.999 | 0.879 | — |
| LAT | 0.999 | 0.869 | — |
| LCP2 | 0.999 | 0.880 | — |
| IRS1 | 0.999 | 0.862 | — |
| PTPN11 | 0.999 | 0.994 | — |
| EGFR | 0.999 | 0.996 | — |
| ERBB2 | 0.999 | 0.934 | — |
| ABL1 | 0.999 | 0.846 | — |
| VAV1 | 0.999 | 0.896 | — |
| IRS2 | 0.999 | 0.372 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000496913.1 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| Gab2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Dnm2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Cd2ap | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Gab1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Vav2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Errfi1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Khdrbs1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Cblb | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Blnk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.7 + PDB: 1AZE, 1BM2, 1BMB, 1CJ1, 1FHS,  | pLDDT=88.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Endosome; Golgi apparatus / Cytosol; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GRB2 — Growth factor receptor-bound protein 2，研究基础较多，新颖性有限。
2. 蛋白大小217 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2898 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2898 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P62993
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177885-GRB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GRB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P62993
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
