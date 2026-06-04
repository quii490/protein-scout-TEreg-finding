---
type: protein-evaluation
gene: "BACH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BACH1 — REJECTED (研究热度过高 (PubMed strict=623，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BACH1 |
| 蛋白名称 | Transcription regulator protein BACH1 |
| 蛋白大小 | 736 aa / 82.0 kDa |
| UniProt ID | O14867 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 736 aa / 82.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=623 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.5; PDB: 2IHC, 8S7D, 8UA3, 8UA6, 8UAH, 8UBT, 8UBU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000210, IPR004827, IPR043321, IPR004826, IPR046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 623 |
| PubMed broad count | 955 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Acute ischemia induces spatially and transcriptionally distinct microglial subclusters.. *Genome medicine*. PMID: 38082331
2. Deletion of BACH1 Attenuates Atherosclerosis by Reducing Endothelial Inflammation.. *Circulation research*. PMID: 35196865
3. Antioxidants stimulate BACH1-dependent tumor angiogenesis.. *The Journal of clinical investigation*. PMID: 37651203
4. Signal amplification in the KEAP1-NRF2-ARE antioxidant response pathway.. *Redox biology*. PMID: 35792437
5. Single-cell multi-omics sequencing uncovers region-specific plasticity of glioblastoma for complementary therapeutic targeting.. *Science advances*. PMID: 39576855

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.5 |
| 高置信度残基 (pLDDT>90) 占比 | 21.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 57.3% |
| 有序区域 (pLDDT>70) 占比 | 36.0% |
| 可用 PDB 条目 | 2IHC, 8S7D, 8UA3, 8UA6, 8UAH, 8UBT, 8UBU, 8UBV, 9GP5, 9GR9 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.5），有序残基占 36.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000210, IPR004827, IPR043321, IPR004826, IPR046347; Pfam: PF00651, PF03131 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAFK | 0.989 | 0.845 | — |
| FBXL17 | 0.980 | 0.782 | — |
| MAFF | 0.913 | 0.669 | — |
| MAFG | 0.894 | 0.860 | — |
| HMMR | 0.881 | 0.822 | — |
| HMOX1 | 0.873 | 0.000 | — |
| MAF | 0.868 | 0.350 | — |
| XPO1 | 0.862 | 0.524 | — |
| MAFB | 0.766 | 0.741 | — |
| FBXO22 | 0.759 | 0.625 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000026703.6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ANAPC5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| BRCA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17525340|imex:IM-19729 |
| ABRAXAS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17525340|imex:IM-19729 |
| HMMR | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| MAFF | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| MAFK | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DYNLL1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| MAFG | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| FAM83D | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.5 + PDB: 2IHC, 8S7D, 8UA3, 8UA6, 8UAH,  | pLDDT=56.5, v6 | 预测+实验 |
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
1. BACH1 — Transcription regulator protein BACH1，研究基础较多，新颖性有限。
2. 蛋白大小736 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 623 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 623 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14867
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156273-BACH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BACH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14867
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
