---
type: protein-evaluation
gene: "NONO"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NONO — REJECTED (研究热度过高 (PubMed strict=521，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NONO / NRB54 |
| 蛋白名称 | Non-POU domain-containing octamer-binding protein |
| 蛋白大小 | 471 aa / 54.2 kDa |
| UniProt ID | Q15233 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Nucleoli fibrillar center; UniProt: Nucleus; Nucleus, nucleolus; Nucleus speckle; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 471 aa / 54.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=521 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.8; PDB: 3SDE, 5IFM, 6WMZ, 7LRQ, 7LRU, 7PU5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012975, IPR012677, IPR034552, IPR035979, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Nucleoli fibrillar center | Enhanced |
| UniProt | Nucleus; Nucleus, nucleolus; Nucleus speckle; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- fibrillar center (GO:0001650)
- membrane (GO:0016020)
- nuclear matrix (GO:0016363)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- paraspeckles (GO:0042382)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 521 |
| PubMed broad count | 1936 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NRB54 |

**关键文献**:
1. Paraspeckle protein NONO attenuates vascular calcification by inhibiting bone morphogenetic protein 2 transcription.. *Kidney international*. PMID: 38417578
2. Remodeling oncogenic transcriptomes by small molecules targeting NONO.. *Nature chemical biology*. PMID: 36864190
3. The landscape of RNA binding proteins in mammalian spermatogenesis.. *Science (New York, N.Y.)*. PMID: 39208083
4. Targeting the splicing factor NONO inhibits GBM progression through GPX1 intron retention.. *Theranostics*. PMID: 35910786
5. LncRNA PSMB8-AS1 Instigates Vascular Inflammation to Aggravate Atherosclerosis.. *Circulation research*. PMID: 38084631

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 54.1% |
| 置信残基 (pLDDT 70-90) 占比 | 10.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 27.4% |
| 有序区域 (pLDDT>70) 占比 | 64.7% |
| 可用 PDB 条目 | 3SDE, 5IFM, 6WMZ, 7LRQ, 7LRU, 7PU5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3SDE, 5IFM, 6WMZ, 7LRQ, 7LRU, 7PU5）+ AlphaFold极高置信度预测（pLDDT=76.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012975, IPR012677, IPR034552, IPR035979, IPR000504; Pfam: PF08075, PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SFPQ | 0.999 | 0.991 | — |
| PSPC1 | 0.999 | 0.988 | — |
| RBM14 | 0.998 | 0.398 | — |
| RBM14-RBM4 | 0.995 | 0.065 | — |
| MATR3-2 | 0.995 | 0.000 | — |
| MATR3 | 0.993 | 0.205 | — |
| FUS | 0.956 | 0.472 | — |
| HNRNPA1 | 0.945 | 0.496 | — |
| HNRNPM | 0.913 | 0.214 | — |
| HNRNPA2B1 | 0.913 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| F5GYZ3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ENSP00000503920.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| FXR2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PIN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAD1L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLEKHF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.8 + PDB: 3SDE, 5IFM, 6WMZ, 7LRQ, 7LRU,  | pLDDT=76.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Nucleus speckle; Chro / Nucleoplasm; 额外: Nucleoli, Nucleoli fibrillar cent | 一致 |
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
1. NONO — Non-POU domain-containing octamer-binding protein，研究基础较多，新颖性有限。
2. 蛋白大小471 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 521 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 521 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15233
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147140-NONO/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NONO
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15233
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
