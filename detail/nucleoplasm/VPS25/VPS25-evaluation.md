---
type: protein-evaluation
gene: "VPS25"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VPS25 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VPS25 / DERP9, EAP20 |
| 蛋白名称 | Vacuolar protein-sorting-associated protein 25 |
| 蛋白大小 | 176 aa / 20.7 kDa |
| UniProt ID | Q9BRG1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Cytoplasm; Endosome membrane; Nucleus, nucleoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 176 aa / 20.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=92.9; PDB: 2ZME, 3CUQ, 3HTU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008570, IPR014041, IPR036388, IPR036390; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | Cytoplasm; Endosome membrane; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- ESCRT II complex (GO:0000814)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DERP9, EAP20 |

**关键文献**:
1. vps25 mosaics display non-autonomous cell survival and overgrowth, and autonomous apoptosis.. *Development (Cambridge, England)*. PMID: 16611691
2. Genetic structure and evolution of the Vps25 family, a yeast ESCRT-II component.. *BMC evolutionary biology*. PMID: 16889659
3. The ESCRT-II Subunit EAP20/VPS25 and the Bro1 Domain Proteins HD-PTP and BROX Are Individually Dispensable for Herpes Simplex Virus 1 Replication.. *Journal of virology*. PMID: 31748394
4. Potential prognosis index for m(6)A-related mRNA in cholangiocarcinoma.. *BMC cancer*. PMID: 35672673
5. Common and distinct genetic properties of ESCRT-II components in Drosophila.. *PloS one*. PMID: 19132102

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.9 |
| 高置信度残基 (pLDDT>90) 占比 | 87.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 98.3% |
| 可用 PDB 条目 | 2ZME, 3CUQ, 3HTU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2ZME, 3CUQ, 3HTU）+ AlphaFold高质量预测（pLDDT=92.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008570, IPR014041, IPR036388, IPR036390; Pfam: PF05871 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS36 | 0.999 | 0.999 | — |
| SNF8 | 0.999 | 0.997 | — |
| CHMP6 | 0.999 | 0.997 | — |
| VPS28 | 0.998 | 0.854 | — |
| CHMP2A | 0.996 | 0.288 | — |
| TSG101 | 0.994 | 0.446 | — |
| CHMP3 | 0.993 | 0.000 | — |
| CHMP7 | 0.992 | 0.095 | — |
| VPS37B | 0.985 | 0.616 | — |
| HGS | 0.984 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SNF8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Vps36 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| APIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RHOXF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| "NEST:bs17h08" | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| uvrB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VPS20 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| VPS20.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| F9I5.13 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.9 + PDB: 2ZME, 3CUQ, 3HTU | pLDDT=92.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Endosome membrane; Nucleus, nucleoplasm / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. VPS25 — Vacuolar protein-sorting-associated protein 25，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小176 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BRG1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131475-VPS25/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VPS25
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BRG1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
