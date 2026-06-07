---
type: protein-evaluation
gene: "RAB3IP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RAB3IP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RAB3IP / RABIN8 |
| 蛋白名称 | Rab-3A-interacting protein |
| 蛋白大小 | 476 aa / 53.0 kDa |
| UniProt ID | Q96QF0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome, Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, cytoskeleton; Cell projection |
| 蛋白大小 | 10/10 | ×1 | 10 | 476 aa / 53.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=70.7; PDB: 4LHX, 4LHY, 4LHZ, 4UJ3, 4UJ4, 4UJ5, 6F6P |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040351, IPR009449; Pfam: PF25555, PF06428 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton; Cell projection, lamellipodium; Vesicle; Cytoplasm, cyt... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- lamellipodium (GO:0030027)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- proximal dendrite (GO:1990635)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RABIN8 |

**关键文献**:
1. Rab3IP interacts with SSX2 and enhances the invasiveness of gastric cancer cells.. *Biochemical and biophysical research communications*. PMID: 30005870
2. The cancer-related protein SSX2 interacts with the human homologue of a Ras-like GTPase interactor, RAB3IP, and a novel nuclear protein, SSX2IP.. *Genes, chromosomes & cancer*. PMID: 12007189
3. Unique Genetic and Epigenetic Alterations in Glioblastoma Long-Term Survivors: Insights From Two Clinical Cases.. *Journal of cellular and molecular medicine*. PMID: 41085137
4. LncRNA HOTAIR targets miR-126-5p to promote the progression of Parkinson's disease through RAB3IP.. *Biological chemistry*. PMID: 30738012
5. MicroRNA‑126 protects SH‑SY5Y cells from ischemia/reperfusion injury‑induced apoptosis by inhibiting RAB3IP.. *Molecular medicine reports*. PMID: 34935056

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.7 |
| 高置信度残基 (pLDDT>90) 占比 | 48.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.6% |
| 低置信 (pLDDT<50) 占比 | 37.0% |
| 有序区域 (pLDDT>70) 占比 | 54.4% |
| 可用 PDB 条目 | 4LHX, 4LHY, 4LHZ, 4UJ3, 4UJ4, 4UJ5, 6F6P |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4LHX, 4LHY, 4LHZ, 4UJ3, 4UJ4, 4UJ5, 6F6P）+ AlphaFold极高置信度预测（pLDDT=70.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040351, IPR009449; Pfam: PF25555, PF06428 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB8A | 0.999 | 0.988 | — |
| RAB11A | 0.999 | 0.980 | — |
| BBS1 | 0.998 | 0.510 | — |
| RAB11FIP3 | 0.990 | 0.916 | — |
| BBS4 | 0.967 | 0.294 | — |
| EXOC6 | 0.961 | 0.409 | — |
| BBIP1 | 0.949 | 0.000 | — |
| BBS5 | 0.933 | 0.000 | — |
| BBS7 | 0.932 | 0.000 | — |
| BBS2 | 0.932 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAB3IL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SSX2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12007189|imex:IM-20236| |
| Rab3a | psi-mi:"MI:0018"(two hybrid) | pubmed:9341137 |
| BBS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14959|pubmed:17574030 |
| BBS4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14959|pubmed:17574030 |
| TRAPPC10 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21273506|imex:IM-17359 |
| TRAPPC9 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21273506|imex:IM-17359 |
| TRAPPC6B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21273506|imex:IM-17359 |
| HSPA1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21273506|imex:IM-17359 |
| TRAPPC6A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21273506|imex:IM-17359 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.7 + PDB: 4LHX, 4LHY, 4LHZ, 4UJ3, 4UJ4,  | pLDDT=70.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton; Cell  / Nucleoplasm; 额外: Centrosome, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RAB3IP — Rab-3A-interacting protein，非常新颖，仅有少数基础研究。
2. 蛋白大小476 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96QF0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127328-RAB3IP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RAB3IP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96QF0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000127328-RAB3IP/subcellular

![](https://images.proteinatlas.org/57728/1006_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/57728/1006_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/57728/1011_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/57728/1011_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/57728/1259_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/57728/1259_B10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96QF0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96QF0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040351;IPR009449; |
| Pfam | PF25555;PF06428; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000127328-RAB3IP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MB21D2 | Intact, Biogrid | true |
| PLOD3 | Intact, Biogrid | true |
| RAB3IL1 | Intact, Biogrid | true |
| RAB8A | Intact, Biogrid | true |
| BANP | Intact | false |
| CHCHD3 | Intact | false |
| FAM124A | Intact | false |
| KRT40 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
