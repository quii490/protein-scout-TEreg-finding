---
type: protein-evaluation
gene: "SUN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUN3 / SUNC1 |
| 蛋白名称 | SUN domain-containing protein 3 |
| 蛋白大小 | 357 aa / 40.5 kDa |
| UniProt ID | Q8TAQ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; UniProt: Membrane; Nucleus envelope; Nucleus inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 357 aa / 40.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045119, IPR012919; Pfam: PF07738 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Approved |
| UniProt | Membrane; Nucleus envelope; Nucleus inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- meiotic nuclear membrane microtubule tethering complex (GO:0034993)
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SUNC1 |

**关键文献**:
1. Evolution and Functional Divergence of SUN Genes in Plants.. *Frontiers in plant science*. PMID: 33763102
2. POD1-SUN-CRT3 chaperone complex guards the ER sorting of LRR receptor kinases in Arabidopsis.. *Nature communications*. PMID: 35577772
3. SUN4 is a spermatid type II inner nuclear membrane protein that forms heteromeric assemblies with SUN3 and interacts with lamin B3.. *Journal of cell science*. PMID: 36825599
4. The testis-specific LINC component SUN3 is essential for sperm head shaping during mouse spermiogenesis.. *The Journal of biological chemistry*. PMID: 32156700
5. In Depth Topological Analysis of Arabidopsis Mid-SUN Proteins and Their Interaction with the Membrane-Bound Transcription Factor MaMYB.. *Plants (Basel, Switzerland)*. PMID: 37176845

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 38.4% |
| 置信残基 (pLDDT 70-90) 占比 | 27.5% |
| 中等置信 (pLDDT 50-70) 占比 | 19.0% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 65.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.0，有序区 65.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045119, IPR012919; Pfam: PF07738 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYNE1 | 0.915 | 0.095 | — |
| SYNE3 | 0.912 | 0.094 | — |
| SYNE2 | 0.835 | 0.091 | — |
| CCDC155 | 0.823 | 0.057 | — |
| SUN5 | 0.780 | 0.000 | — |
| SYNE4 | 0.749 | 0.000 | — |
| SPAG4 | 0.687 | 0.095 | — |
| SUN1 | 0.659 | 0.000 | — |
| C7orf57 | 0.656 | 0.071 | — |
| ODF1 | 0.645 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GAS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LAPTM4A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TBC1D9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PCYOX1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| XYLT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ADGRL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 无 | pLDDT=76.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Nucleus envelope; Nucleus inner membrane / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SUN3 — SUN domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小357 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TAQ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164744-SUN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TAQ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000164744-SUN3/subcellular

![](https://images.proteinatlas.org/76890/1950_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/76890/1950_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/76890/2154_F12_4_red_green.jpg)
![](https://images.proteinatlas.org/76890/2154_F12_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TAQ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TAQ9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 193..354; /note="SUN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00802" |
| InterPro | IPR045119;IPR012919; |
| Pfam | PF07738; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164744-SUN3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
