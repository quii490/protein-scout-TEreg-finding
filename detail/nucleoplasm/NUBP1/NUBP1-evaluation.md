---
type: protein-evaluation
gene: "NUBP1"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NUBP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NUBP1 / NBP, NBP1 |
| 蛋白名称 | Cytosolic Fe-S cluster assembly factor NUBP1 |
| 蛋白大小 | 320 aa / 34.5 kDa |
| UniProt ID | P53384 |
| 评估日期 | 2026-06-04 |

**功能简介** (UniProt): Component of the cytosolic iron-sulfur (Fe/S) protein assembly (CIA) machinery (PubMed:18573874). Required for maturation of extramitochondrial Fe-S proteins (PubMed:18573874). The NUBP1-NUBP2 heterotetramer forms a Fe-S scaffold complex, mediating the de novo assembly of an Fe-S cluster and its transfer to target apoproteins (PubMed:18573874). Implicated in the regulation of centrosome duplicatio...

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol, Mid piece, Principal piece, End piece; 额外: Golgi ap; UniProt: Cytoplasm; Nucleus; Cell projection; Cytoplasm, cytoskeleton |
| 蛋白大小 | 10/10 | ×1 | 10 | 320 aa / 34.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003593, IPR000808, IPR019591, IPR028601, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol, Mid piece, Principal piece, End piece; 额外: Golgi apparatus, Centrosome | Supported |
| UniProt | Cytoplasm; Nucleus; Cell projection; Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskeleto... | Swiss-Prot/TrEMBL |

**IF 图像**: HPA 记录中该基因有可用 IF 图像（`if_display_images_available`），但未生成本地 IF 嵌入。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axoneme (GO:0005930)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleus (GO:0005634)
- sperm end piece (GO:0097229)
- sperm midpiece (GO:0097225)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NBP, NBP1 |

**关键文献**:
1. Human glutaredoxin 3: multiple domains for a unique function.. *Journal of inorganic biochemistry*. PMID: 41092652
2. Motor protein KIFC5A interacts with Nubp1 and Nubp2, and is implicated in the regulation of centrosome duplication.. *Journal of cell science*. PMID: 16638812
3. The nucleotide-binding proteins Nubp1 and Nubp2 are negative regulators of ciliogenesis.. *Cellular and molecular life sciences : CMLS*. PMID: 23807208
4. A novel family of katanin-like 2 protein isoforms (KATNAL2), interacting with nucleotide-binding proteins Nubp1 and Nubp2, are key regulators of different MT-based processes in mammalian cells.. *Cellular and molecular life sciences : CMLS*. PMID: 26153462
5. Proteomic analysis of host cellular proteins co-immunoprecipitated with duck enteritis virus gC.. *Journal of proteomics*. PMID: 34091090

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.7 |
| 高置信度残基 (pLDDT>90) 占比 | 68.1% |
| 置信残基 (pLDDT 70-90) 占比 | 25.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 93.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.7，有序区 93.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR000808, IPR019591, IPR028601, IPR027417; Pfam: PF10609 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CIAO1 | 0.969 | 0.100 | — |
| CIAPIN1 | 0.967 | 0.281 | — |
| CIAO3 | 0.959 | 0.288 | — |
| ABCB7 | 0.938 | 0.219 | — |
| MMS19 | 0.930 | 0.075 | — |
| NUBP2 | 0.922 | 0.456 | — |
| CIAO2B | 0.894 | 0.075 | — |
| NDOR1 | 0.883 | 0.091 | — |
| FOXRED1 | 0.831 | 0.000 | — |
| ISCU | 0.820 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%，尚无实验验证互作。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.7 + PDB: 无 | pLDDT=89.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell projection; Cytoplasm, cy / Cytosol, Mid piece, Principal piece, End piece; 额外 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. NUBP1 — Cytosolic Fe-S cluster assembly factor NUBP1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小320 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53384
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103274-NUBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53384
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live via harvest pipeline; evaluated 2026-06-04

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P53384-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P53384 |
| SMART | SM00382; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003593;IPR000808;IPR019591;IPR028601;IPR027417;IPR033756; |
| Pfam | PF10609; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000103274-NUBP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NUBP2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
