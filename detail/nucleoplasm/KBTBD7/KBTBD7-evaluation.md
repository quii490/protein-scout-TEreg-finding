---
type: protein-evaluation
gene: "KBTBD7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KBTBD7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KBTBD7 |
| 蛋白名称 | Kelch repeat and BTB domain-containing protein 7 |
| 蛋白大小 | 684 aa / 77.2 kDa |
| UniProt ID | Q8WVZ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 684 aa / 77.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR046790, IPR047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Linear ubiquitination at damaged lysosomes induces local NFKB activation and controls cell survival.. *Autophagy*. PMID: 39744815
2. The KBTBD6/7-DRD2 axis regulates pituitary adenoma sensitivity to dopamine agonist treatment.. *Acta neuropathologica*. PMID: 32572597
3. KBTBD7, a novel human BTB-kelch protein, activates transcriptional activities of SRE and AP-1.. *BMB reports*. PMID: 20132730
4. New TFII-I family target genes involved in embryonic development.. *Biochemical and biophysical research communications*. PMID: 19527686
5. Crocin inhibits KBTBD7 to prevent excessive inflammation and cardiac dysfunction following myocardial infarction.. *Molecular medicine reports*. PMID: 36484363

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.6 |
| 高置信度残基 (pLDDT>90) 占比 | 54.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 15.2% |
| 有序区域 (pLDDT>70) 占比 | 77.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.6，有序区 77.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR046790, IPR047931; Pfam: PF07707, PF00651, PF20165 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.998 | 0.835 | — |
| KBTBD6 | 0.995 | 0.809 | — |
| KBTBD8 | 0.949 | 0.448 | — |
| RBX1 | 0.941 | 0.322 | — |
| SPOPL | 0.921 | 0.084 | — |
| KCTD17 | 0.914 | 0.069 | — |
| KLHL9 | 0.912 | 0.000 | — |
| KLHL42 | 0.911 | 0.062 | — |
| KLHL8 | 0.910 | 0.000 | — |
| KLHL20 | 0.910 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000368797.3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| BLMH | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BARD1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| CEP126 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| LINC00341 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MAP1LC3B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NFKBIE | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CPT1A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBXN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.6 + PDB: 无 | pLDDT=80.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KBTBD7 — Kelch repeat and BTB domain-containing protein 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小684 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WVZ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120696-KBTBD7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KBTBD7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WVZ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WVZ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WVZ9 |
| SMART | SM00875;SM00225;SM00612; |
| UniProt Domain [FT] | DOMAIN 63..138; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037" |
| InterPro | IPR011705;IPR017096;IPR000210;IPR046790;IPR047931;IPR047933;IPR015915;IPR006652;IPR011333; |
| Pfam | PF07707;PF00651;PF20165;PF01344; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120696-KBTBD7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBXL17 | Biogrid, Bioplex | true |
| GABARAP | Intact, Biogrid | true |
| GABARAPL1 | Intact, Biogrid | true |
| GABARAPL2 | Intact, Biogrid | true |
| KBTBD6 | Intact, Biogrid, Bioplex | true |
| KBTBD8 | Intact, Biogrid | true |
| LLGL1 | Biogrid, Bioplex | true |
| MAP1LC3B | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
