---
type: protein-evaluation
gene: "RARA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RARA — REJECTED (研究热度过高 (PubMed strict=992，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RARA / NR1B1 |
| 蛋白名称 | Retinoic acid receptor alpha |
| 蛋白大小 | 462 aa / 50.8 kDa |
| UniProt ID | P10276 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Actin filaments, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 462 aa / 50.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=992 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.1; PDB: 1DKF, 1DSZ, 3A9E, 3KMR, 3KMZ, 4DQM, 5K13 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035500, IPR047159, IPR047158, IPR000536, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Actin filaments, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 992 |
| PubMed broad count | 4754 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR1B1 |

**关键文献**:
1. Acute promyelocytic leukemia current treatment algorithms.. *Blood cancer journal*. PMID: 34193815
2. Function of PML-RARA in Acute Promyelocytic Leukemia.. *Advances in experimental medicine and biology*. PMID: 39017850
3. Genotypic and Phenotypic Characteristics of Acute Promyelocytic Leukemia Translocation Variants.. *Hematology/oncology and stem cell therapy*. PMID: 32473106
4. UBR5 forms ligand-dependent complexes on chromatin to regulate nuclear hormone receptor stability.. *Molecular cell*. PMID: 37478846
5. Acute Promyelocytic Leukemia: A Constellation of Molecular Events around a Single PML-RARA Fusion Gene.. *Cancers*. PMID: 32182684

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.1 |
| 高置信度残基 (pLDDT>90) 占比 | 58.7% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 24.2% |
| 有序区域 (pLDDT>70) 占比 | 67.8% |
| 可用 PDB 条目 | 1DKF, 1DSZ, 3A9E, 3KMR, 3KMZ, 4DQM, 5K13, 6XWG, 7AOS, 7APO |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1DKF, 1DSZ, 3A9E, 3KMR, 3KMZ, 4DQM, 5K13, 6XWG, 7AOS, 7APO）+ AlphaFold极高置信度预测（pLDDT=78.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035500, IPR047159, IPR047158, IPR000536, IPR001723; Pfam: PF00104, PF00105 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCOR1 | 0.999 | 0.988 | — |
| NCOR2 | 0.999 | 0.856 | — |
| RXRA | 0.999 | 0.991 | — |
| PML | 0.998 | 0.837 | — |
| ZBTB16 | 0.997 | 0.311 | — |
| NCOA1 | 0.996 | 0.989 | — |
| RXRB | 0.993 | 0.862 | — |
| NCOA2 | 0.992 | 0.980 | — |
| RARB | 0.984 | 0.921 | — |
| RXRG | 0.983 | 0.848 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RXRG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Ncoa6 | psi-mi:"MI:0096"(pull down) | pubmed:10866662 |
| RXRB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Trim24 | psi-mi:"MI:0018"(two hybrid) | pubmed:8978696 |
| cadB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| napH | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| potC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| rplL | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| yihN | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| UBE3A | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.1 + PDB: 1DKF, 1DSZ, 3A9E, 3KMR, 3KMZ,  | pLDDT=78.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Nucleoli, Actin filaments, Cytoso | 一致 |
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
1. RARA — Retinoic acid receptor alpha，研究基础较多，新颖性有限。
2. 蛋白大小462 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 992 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 992 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P10276
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131759-RARA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RARA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P10276
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
