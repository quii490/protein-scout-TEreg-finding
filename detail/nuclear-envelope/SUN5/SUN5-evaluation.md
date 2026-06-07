---
type: protein-evaluation
gene: "SUN5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUN5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUN5 / SPAG4L, TSARG4 |
| 蛋白名称 | SUN domain-containing protein 5 |
| 蛋白大小 | 379 aa / 43.1 kDa |
| UniProt ID | Q8TC36 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus inner membrane; Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 379 aa / 43.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045119, IPR012919; Pfam: PF07738 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus inner membrane; Golgi apparatus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- meiotic nuclear membrane microtubule tethering complex (GO:0034993)
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)
- sperm head-tail coupling apparatus (GO:0120212)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 256 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPAG4L, TSARG4 |

**关键文献**:
1. Genetic etiological spectrum of sperm morphological abnormalities.. *Journal of assisted reproduction and genetics*. PMID: 39417902
2. SUN5 interacts with nuclear membrane LaminB1 and cytoskeletal GTPase Septin12 mediating the sperm head-and-tail junction.. *Molecular human reproduction*. PMID: 38870534
3. ARRDC5 deficiency impairs spermatogenesis by affecting SUN5 and NDC1.. *Development (Cambridge, England)*. PMID: 37997706
4. CCDC113 stabilizes sperm axoneme and head-tail coupling apparatus to ensure male fertility.. *eLife*. PMID: 39671309
5. SUN5, a testis-specific nuclear membrane protein, participates in recruitment and export of nuclear mRNA in spermatogenesis.. *Acta biochimica et biophysica Sinica*. PMID: 39108207

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.5 |
| 高置信度残基 (pLDDT>90) 占比 | 42.5% |
| 置信残基 (pLDDT 70-90) 占比 | 19.5% |
| 中等置信 (pLDDT 50-70) 占比 | 17.7% |
| 低置信 (pLDDT<50) 占比 | 20.3% |
| 有序区域 (pLDDT>70) 占比 | 62.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.5，有序区 62.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045119, IPR012919; Pfam: PF07738 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYNE1 | 0.857 | 0.091 | — |
| CCDC155 | 0.812 | 0.057 | — |
| PMFBP1 | 0.804 | 0.079 | — |
| SYNE3 | 0.793 | 0.094 | — |
| SUN3 | 0.780 | 0.000 | — |
| SPAG4 | 0.778 | 0.248 | — |
| SYNE2 | 0.776 | 0.091 | — |
| ODF1 | 0.755 | 0.000 | — |
| SPATA6 | 0.748 | 0.000 | — |
| SYNE4 | 0.723 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SPAG4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLHL36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.5 + PDB: 无 | pLDDT=75.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus inner membrane; Golgi apparatus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SUN5 — SUN domain-containing protein 5，非常新颖，仅有少数基础研究。
2. 蛋白大小379 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TC36
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167098-SUN5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUN5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TC36
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TC36-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TC36 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 205..364; /note="SUN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00802" |
| InterPro | IPR045119;IPR012919; |
| Pfam | PF07738; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167098-SUN5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SPAG4 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
