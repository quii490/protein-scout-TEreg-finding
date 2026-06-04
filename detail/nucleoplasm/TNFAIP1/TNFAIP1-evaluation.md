---
type: protein-evaluation
gene: "TNFAIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TNFAIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TNFAIP1 / BACURD2, EDP1 |
| 蛋白名称 | BTB/POZ domain-containing adapter for CUL3-mediated RhoA degradation protein 2 |
| 蛋白大小 | 316 aa / 36.2 kDa |
| UniProt ID | Q13829 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: Cytoplasm; Nucleus; Endosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 316 aa / 36.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=69 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045068, IPR000210, IPR011333, IPR003131; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | Cytoplasm; Nucleus; Endosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endosome (GO:0005768)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 69 |
| PubMed broad count | 91 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BACURD2, EDP1 |

**关键文献**:
1. Neuronal-specific TNFAIP1 ablation attenuates postoperative cognitive dysfunction via targeting SNAP25 for K48-linked ubiquitination.. *Cell communication and signaling : CCS*. PMID: 38102610
2. CRISPR/Cas9-Mediated Knockout of tnfaip1 in Zebrafish Plays a Role in Early Development.. *Genes*. PMID: 37239365
3. TNFAIP1 promotes macrophage lipid accumulation and accelerates the development of atherosclerosis through the LEENE/FoxO1/ABCA1 pathway.. *Journal of physiology and biochemistry*. PMID: 38878215
4. Knocking down TNFAIP1 alleviates inflammation and oxidative stress in pediatric pneumonia through PI3K/Akt/Nrf2 pathway.. *Allergologia et immunopathologia*. PMID: 37422785
5. Interaction between microRNA-181a and TNFAIP1 regulates pancreatic cancer proliferation and migration.. *Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine*. PMID: 26152285

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.0 |
| 高置信度残基 (pLDDT>90) 占比 | 61.7% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 17.1% |
| 有序区域 (pLDDT>70) 占比 | 74.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.0，有序区 74.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045068, IPR000210, IPR011333, IPR003131; Pfam: PF02214 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAF1 | 0.995 | 0.994 | — |
| UBXN7 | 0.995 | 0.994 | — |
| UBXN1 | 0.995 | 0.994 | — |
| CUL3 | 0.993 | 0.790 | — |
| KCTD13 | 0.989 | 0.893 | — |
| KCTD10 | 0.975 | 0.873 | — |
| RBX1 | 0.941 | 0.364 | — |
| KCTD17 | 0.920 | 0.000 | — |
| KLHL20 | 0.919 | 0.000 | — |
| KLHL12 | 0.914 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000226225.2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POLR1C | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ARNT | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| KCTD13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| RHOB | psi-mi:"MI:0018"(two hybrid) | pubmed:19637314|imex:IM-20406 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| UBXN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FLNC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCTD10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.0 + PDB: 无 | pLDDT=81.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Endosome / Nucleoli | 一致 |
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
1. TNFAIP1 — BTB/POZ domain-containing adapter for CUL3-mediated RhoA degradation protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小316 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 69 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13829
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109079-TNFAIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TNFAIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13829
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
