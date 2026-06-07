---
type: protein-evaluation
gene: "DNAAF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAAF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAAF2 / C14orf104, KTU |
| 蛋白名称 | Protein kintoun |
| 蛋白大小 | 837 aa / 91.1 kDa |
| UniProt ID | Q9NVR5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Basal body, Cytosol; 额外: Nucleoli, Golgi apparatus, Primary ; UniProt: Cytoplasm; Dynein axonemal particle |
| 蛋白大小 | 8/10 | ×1 | 8 | 837 aa / 91.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034727, IPR050734, IPR012981, IPR041442; Pfam:  |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.0/180** | |
| **归一化总分** | | | **79.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Basal body, Cytosol; 额外: Nucleoli, Golgi apparatus, Primary cilium | Approved |
| UniProt | Cytoplasm; Dynein axonemal particle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dynein axonemal particle (GO:0120293)
- extracellular region (GO:0005576)
- Golgi apparatus (GO:0005794)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf104, KTU |

**关键文献**:
1. Primary Ciliary Dyskinesia.. **. PMID: 20301301
2. Novel Gene Variants Associated with Primary Ciliary Dyskinesia.. *Indian journal of pediatrics*. PMID: 35239159
3. A null allele of Dnaaf2 displays embryonic lethality and mimics human ciliary dyskinesia.. *Human molecular genetics*. PMID: 31107948
4. Novel compound heterozygous DNAAF2 mutations cause primary ciliary dyskinesia in a Han Chinese family.. *Journal of assisted reproduction and genetics*. PMID: 32638265
5. Establishment of the early cilia preassembly protein complex during motile ciliogenesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 29358401

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.2 |
| 高置信度残基 (pLDDT>90) 占比 | 31.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 43.2% |
| 有序区域 (pLDDT>70) 占比 | 48.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.2），有序残基占 48.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034727, IPR050734, IPR012981, IPR041442; Pfam: PF08190, PF18201 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAI2 | 0.970 | 0.000 | — |
| DNAI1 | 0.958 | 0.000 | — |
| DNAAF1 | 0.939 | 0.000 | — |
| RSPH4A | 0.933 | 0.000 | — |
| RSPH9 | 0.926 | 0.000 | — |
| DNAH5 | 0.916 | 0.000 | — |
| PIH1D3 | 0.910 | 0.000 | — |
| NME8 | 0.900 | 0.000 | — |
| DNAH11 | 0.898 | 0.000 | — |
| DNAAF4 | 0.883 | 0.206 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MEMO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| UBE3D | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PRPF38A | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DNAAF10 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CALM1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DNAAF4 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DEFA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NFATC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHDC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 6 / 15 = 40%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 40%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.2 + PDB: 无 | pLDDT=64.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Dynein axonemal particle / Basal body, Cytosol; 额外: Nucleoli, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAAF2 — Protein kintoun，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小837 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVR5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165506-DNAAF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAAF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVR5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Basal body (uncertain)。来源: https://www.proteinatlas.org/ENSG00000165506-DNAAF2/subcellular

![](https://images.proteinatlas.org/2894/2185_A6_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/2894/2185_A6_66_blue_red_green.jpg)
![](https://images.proteinatlas.org/2894/2186_C5_67_blue_red_green.jpg)
![](https://images.proteinatlas.org/2894/2186_C5_78_blue_red_green.jpg)
![](https://images.proteinatlas.org/2894/2201_C6_53_blue_red_green.jpg)
![](https://images.proteinatlas.org/2894/2201_C6_76_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVR5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NVR5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR034727;IPR050734;IPR012981;IPR041442; |
| Pfam | PF08190;PF18201; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165506-DNAAF2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| UBE3D | Intact, Biogrid | true |
| AIP | Biogrid | false |
| CSNK2A2 | Opencell | false |
| DNAAF10 | Intact | false |
| DNAAF4 | Intact | false |
| PRPF38A | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
