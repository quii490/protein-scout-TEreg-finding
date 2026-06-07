---
type: protein-evaluation
gene: "PIF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PIF1 — REJECTED (研究热度过高 (PubMed strict=274，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PIF1 / C15orf20 |
| 蛋白名称 | ATP-dependent DNA helicase PIF1 |
| 蛋白大小 | 641 aa / 69.8 kDa |
| UniProt ID | Q9H611 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 641 aa / 69.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=274 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.0; PDB: 5FHH, 6HPH, 6HPQ, 6HPT, 6HPU, 9FB8, 9FI9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010285, IPR027417, IPR049163, IPR057437, IPR051 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- mitochondrial nucleoid (GO:0042645)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 274 |
| PubMed broad count | 534 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf20 |

**关键文献**:
1. Structure and function of Pif1 helicase.. *Biochemical Society transactions*. PMID: 28900015
2. RNF4 sustains Myc-driven tumorigenesis by facilitating DNA replication.. *The Journal of clinical investigation*. PMID: 38530355
3. Pif1 Helicases and the Evidence for a Prokaryotic Origin of Helitrons.. *Molecular biology and evolution*. PMID: 34850089
4. Pif1 Activity is Modulated by DNA Sequence and Structure.. *Biochemistry*. PMID: 34932305
5. Dynamic regulation of Pif1 acetylation is crucial to the maintenance of genome stability.. *Current genetics*. PMID: 33079209

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 39.6% |
| 置信残基 (pLDDT 70-90) 占比 | 37.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 77.2% |
| 可用 PDB 条目 | 5FHH, 6HPH, 6HPQ, 6HPT, 6HPU, 9FB8, 9FI9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5FHH, 6HPH, 6HPQ, 6HPT, 6HPU, 9FB8, 9FI9）+ AlphaFold极高置信度预测（pLDDT=78.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010285, IPR027417, IPR049163, IPR057437, IPR051055; Pfam: PF25344, PF05970, PF21530 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNA2 | 0.962 | 0.767 | — |
| ORC5 | 0.915 | 0.840 | — |
| RAD52 | 0.912 | 0.624 | — |
| PCNA | 0.912 | 0.850 | — |
| TERT | 0.907 | 0.284 | — |
| WRN | 0.891 | 0.417 | — |
| PRH1 | 0.885 | 0.000 | — |
| PRH2 | 0.883 | 0.000 | — |
| RAD51 | 0.878 | 0.486 | — |
| RECQL4 | 0.866 | 0.495 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| "Fs | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Ten-m | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| cold | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| NOP9 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| SSA3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| YDJ1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SEC63 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| HSP78 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 5FHH, 6HPH, 6HPQ, 6HPT, 6HPU,  | pLDDT=78.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Mitochondrion / Nucleoplasm | 一致 |
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
1. PIF1 — ATP-dependent DNA helicase PIF1，研究基础较多，新颖性有限。
2. 蛋白大小641 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 274 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 274 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H611
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140451-PIF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PIF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H611
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/PIF1/IF_images/PIF1_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000140451-PIF1/subcellular

![](https://images.proteinatlas.org/18701/944_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/18701/944_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/18701/947_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/18701/947_F4_4_red_green.jpg)
![](https://images.proteinatlas.org/18701/952_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/18701/952_F4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H611-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H611 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010285;IPR027417;IPR049163;IPR057437;IPR051055;IPR048293; |
| Pfam | PF25344;PF05970;PF21530; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140451-PIF1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
