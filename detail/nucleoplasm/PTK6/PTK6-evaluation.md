---
type: protein-evaluation
gene: "PTK6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PTK6 — REJECTED (研究热度过高 (PubMed strict=187，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTK6 / BRK |
| 蛋白名称 | Protein-tyrosine kinase 6 |
| 蛋白大小 | 451 aa / 51.8 kDa |
| UniProt ID | Q13882 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus; Cell projection, ruffle; Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 451 aa / 51.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=187 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.8; PDB: 1RJA, 2KGT, 5D7V, 5DA3, 5H2U, 6CZ2, 6CZ3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009, IPR050198, IPR000719, IPR017441, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cell projection, ruffle; Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- ruffle (GO:0001726)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 187 |
| PubMed broad count | 295 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRK |

**关键文献**:
1. PTK6 drives HNRNPH1 phase separation to activate autophagy and suppress apoptosis in colorectal cancer.. *Autophagy*. PMID: 40103198
2. Targeting protein tyrosine kinase 6 in cancer.. *Biochimica et biophysica acta. Reviews on cancer*. PMID: 32956764
3. A PROTAC degrader suppresses oncogenic functions of PTK6, inducing apoptosis of breast cancer cells.. *Cell chemical biology*. PMID: 39541980
4. Context-specific protein tyrosine kinase 6 (PTK6) signalling in prostate cancer.. *European journal of clinical investigation*. PMID: 23398121
5. Kinase-Dependent and -Independent Roles for PTK6 in Colon Cancer.. *Molecular cancer research : MCR*. PMID: 26983689

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.8 |
| 高置信度残基 (pLDDT>90) 占比 | 60.3% |
| 置信残基 (pLDDT 70-90) 占比 | 33.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 94.0% |
| 可用 PDB 条目 | 1RJA, 2KGT, 5D7V, 5DA3, 5H2U, 6CZ2, 6CZ3, 6CZ4, 8S1C |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1RJA, 2KGT, 5D7V, 5DA3, 5H2U, 6CZ2, 6CZ3, 6CZ4, 8S1C）+ AlphaFold极高置信度预测（pLDDT=88.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR050198, IPR000719, IPR017441, IPR035846; Pfam: PF07714, PF00017, PF00018 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STAP2 | 0.996 | 0.292 | — |
| EGFR | 0.989 | 0.624 | — |
| KHDRBS1 | 0.988 | 0.611 | — |
| GPNMB | 0.978 | 0.292 | — |
| BCAR1 | 0.943 | 0.071 | — |
| PXN | 0.943 | 0.061 | — |
| SOCS3 | 0.941 | 0.328 | — |
| ARHGAP35 | 0.941 | 0.067 | — |
| LRRK2 | 0.930 | 0.051 | — |
| AKT1 | 0.927 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0424"(protein kinase assay) | pubmed:21481795|imex:IM-16879 |
| EBI-1381002 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1380984 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| CDC37 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| CCT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| KHDRBS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| CCT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| CCT4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| CCT8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.8 + PDB: 1RJA, 2KGT, 5D7V, 5DA3, 5H2U,  | pLDDT=88.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell projection, ruffle; Membr / Nucleoplasm; 额外: Nuclear bodies, Plasma membrane,  | 一致 |
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
1. PTK6 — Protein-tyrosine kinase 6，研究基础较多，新颖性有限。
2. 蛋白大小451 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 187 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 187 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13882
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101213-PTK6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTK6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13882
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/PTK6/PTK6-PAE.png]]
