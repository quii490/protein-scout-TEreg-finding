---
type: protein-evaluation
gene: "DLK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DLK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLK2 / EGFL9 |
| 蛋白名称 | Protein delta homolog 2 |
| 蛋白大小 | 383 aa / 40.5 kDa |
| UniProt ID | Q6UY11 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli, Vesicles; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 383 aa / 40.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000742, IPR001881, IPR000152, IPR018097, IPR051 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EGFL9 |

**关键文献**:
1. Delta-like 2 negatively regulates chondrogenic differentiation.. *Journal of cellular physiology*. PMID: 29057471
2. Multi-omics analysis identifies diagnostic circulating biomarkers and potential therapeutic targets, revealing IQGAP1 as an oncogene in gastric cancer.. *NPJ precision oncology*. PMID: 40229327
3. Dlk2 interacts with Syap1 to activate Akt signaling pathway during osteoclast formation.. *Cell death & disease*. PMID: 37669921
4. DLK2 is a transcriptional target of KLF4 in the early stages of adipogenesis.. *Journal of molecular biology*. PMID: 22306741
5. The novel gene EGFL9/Dlk2, highly homologous to Dlk1, functions as a modulator of adipogenesis.. *Journal of molecular biology*. PMID: 17320102

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 45.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 30.8% |
| 有序区域 (pLDDT>70) 占比 | 65.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.8，有序区 65.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000742, IPR001881, IPR000152, IPR018097, IPR051022; Pfam: PF00008, PF21700 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTC28 | 0.601 | 0.099 | — |
| KTN1 | 0.566 | 0.100 | — |
| EGFL8 | 0.507 | 0.000 | — |
| MEGF9 | 0.482 | 0.000 | — |
| NOTCH1 | 0.444 | 0.351 | — |
| NKAIN1 | 0.424 | 0.000 | — |
| KARS1 | 0.408 | 0.045 | — |
| NGFR | 0.402 | 0.000 | — |
| EGFL7 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ADAMTSL4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SLC22A23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LDLR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HLA-A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STAT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NOTCH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| METAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRBA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 15
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 无 | pLDDT=73.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Nucleoli, Vesicles | 一致 |
| PPI | STRING + IntAct | 9 + 15 interactions | 数据充分 |

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
1. DLK2 — Protein delta homolog 2，非常新颖，仅有少数基础研究。
2. 蛋白大小383 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UY11
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171462-DLK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UY11
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000171462-DLK2/subcellular

![](https://images.proteinatlas.org/68672/1365_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/68672/1365_F8_6_red_green.jpg)
![](https://images.proteinatlas.org/70955/1324_D11_10_red_green.jpg)
![](https://images.proteinatlas.org/70955/1324_D11_6_red_green.jpg)
![](https://images.proteinatlas.org/70955/1325_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/70955/1325_D11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6UY11-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UY11 |
| SMART | SM00181;SM00179; |
| UniProt Domain [FT] | DOMAIN 27..58; /note="EGF-like 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 62..89; /note="EGF-like 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 91..129; /note="EGF-like 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 131..172; /note="EGF-like 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 174..210; /note="EGF-like 5; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 212..248; /note="EGF-like 6; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076" |
| InterPro | IPR000742;IPR001881;IPR000152;IPR018097;IPR051022; |
| Pfam | PF00008;PF21700; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171462-DLK2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
