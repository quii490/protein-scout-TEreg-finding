---
type: protein-evaluation
gene: "EIF5A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF5A — REJECTED (研究热度过高 (PubMed strict=602，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF5A |
| 蛋白名称 | Eukaryotic translation initiation factor 5A-1 |
| 蛋白大小 | 154 aa / 16.8 kDa |
| UniProt ID | P63241 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Plasma membrane; UniProt: Cytoplasm; Nucleus; Endoplasmic reticulum membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 154 aa / 16.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=602 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.6; PDB: 3CPF, 5DLQ, 8A0E, 8Y0W |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001884, IPR048670, IPR020189, IPR012340, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Plasma membrane | Supported |
| UniProt | Cytoplasm; Nucleus; Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- annulate lamellae (GO:0005642)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- nuclear pore (GO:0005643)
- nucleus (GO:0005634)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 602 |
| PubMed broad count | 821 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Polyglutamine-mediated ribotoxicity disrupts proteostasis and stress responses in Huntington's disease.. *Nature cell biology*. PMID: 38741019
2. A molecular network of conserved factors keeps ribosomes dormant in the egg.. *Nature*. PMID: 36653451
3. Arachidonic acid triggers spermidine synthase secretion from primary tumor to induce skeletal muscle weakness upon irradiation.. *Cell metabolism*. PMID: 40541182
4. Polyamine and EIF5A hypusination downstream of c-Myc confers targeted therapy resistance in BRAF mutant melanoma.. *Molecular cancer*. PMID: 38965534
5. Spermidine-mediated hypusination of translation factor EIF5A improves mitochondrial fatty acid oxidation and prevents non-alcoholic steatohepatitis progression.. *Nature communications*. PMID: 36057633

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.6 |
| 高置信度残基 (pLDDT>90) 占比 | 79.9% |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 5.2% |
| 有序区域 (pLDDT>70) 占比 | 90.3% |
| 可用 PDB 条目 | 3CPF, 5DLQ, 8A0E, 8Y0W |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3CPF, 5DLQ, 8A0E, 8Y0W）+ AlphaFold高质量预测（pLDDT=88.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001884, IPR048670, IPR020189, IPR012340, IPR014722; Pfam: PF01287, PF21485 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DOHH | 0.999 | 0.772 | — |
| DHPS | 0.999 | 0.799 | — |
| FAU | 0.997 | 0.993 | — |
| EEF2 | 0.996 | 0.898 | — |
| RPL5 | 0.995 | 0.966 | — |
| RPL23A | 0.994 | 0.973 | — |
| RPS11 | 0.994 | 0.955 | — |
| RPS3 | 0.994 | 0.955 | — |
| RPL35 | 0.993 | 0.955 | — |
| RPL23 | 0.993 | 0.955 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UPS2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TRP2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| LIA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| DJP1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| XRN2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| Hnrnpk | psi-mi:"MI:0096"(pull down) | pubmed:16518874|imex:IM-11840 |
| IQCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| gerLA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.6 + PDB: 3CPF, 5DLQ, 8A0E, 8Y0W | pLDDT=88.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Endoplasmic reticulum membrane / Cytosol; 额外: Nucleoplasm, Plasma membrane | 一致 |
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
1. EIF5A — Eukaryotic translation initiation factor 5A-1，研究基础较多，新颖性有限。
2. 蛋白大小154 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 602 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 602 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P63241
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132507-EIF5A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF5A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P63241
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P63241-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
