---
type: protein-evaluation
gene: "TNIP2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TNIP2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TNIP2 / ABIN-2|MGC4289|KLIP|FLIP1|ABIN2 |
| 蛋白全称 | TNFAIP3-interacting protein 2 |
| 蛋白大小 | 429 aa |
| UniProt ID | Q8NFZ5 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TNIP2/IF_images/MCF-7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TNIP2/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 429 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 50 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 4 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5) |
|  | **原始总分** |  | **113/183** | **112.0/183** |  |  |  |
|  | **归一化总分** |  | **61.7/100** | **61.2/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Cytoplasm, Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 429 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 50 |

**评价**: PubMed 50 篇，高度新颖

**关键文献**:
1. Ishigaki K et al. (2022). "Multi-ancestry genome-wide association analyses identify novel genetic mechanisms in rheumatoid arthritis". *Nat Genet*. PMID: 36333501
2. Qian X et al. (2023). "TNFAIP3 interacting protein 2 relieves lipopolysaccharide (LPS)-induced inflammatory injury in endometritis by inhibiting NF-kappaB activation". *Immun Inflamm Dis*. PMID: 37904691
3. Chen L et al. (2023). "TNIP2 inhibits amyloidogenesis by regulating the 3'UTR of BACE1: An in vitro study". *Neurosci Lett*. PMID: 37085111
4. Yan Z et al. (2021). "Neuroprotective Function of TNFAIP3 Interacting Protein 2 Against Oxygen and Glucose Deprivation/Reoxygenation-Induced Injury in Hippocampal Neuronal HT22 Cells Through Regulation of the TLR4/MyD88...". *Neuropsychiatr Dis Treat*. PMID: 34267521
5. Laubhahn K et al. (2022). "17q12-21 risk-variants influence cord blood immune regulation and multitrigger-wheeze". *Pediatr Allergy Immunol*. PMID: 34919286
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 429 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 4 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TNIP2/TNIP2-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | EABR |
| InterPro | NEMO_ZF |
| Pfam | EABR |
| PROSITE | ZF_CCHC_NOA |

**染色质调控潜力分析**: 4 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| MAP3K8 | tandem affinity purification | 14743216 | — | — |
| REL | tandem affinity purification | 14743216 | — | — |
| NFKB2 | tandem affinity purification | 14743216 | — | — |
| RELA | tandem affinity purification | 14743216 | — | — |
| NFKB1 | two hybrid | 21988832 | — | — |
| MAPK1 | two hybrid | 21988832 | — | — |
| IKBKG | two hybrid | 21988832 | — | — |
| MKNK1 | two hybrid | 21988832 | — | — |
| PDCD6IP | two hybrid | 21988832 | — | — |
| CDKN1A | two hybrid | 21988832 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 4 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 50 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TNIP2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168884-TNIP2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TNIP2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8NFZ5
- STRING: https://string-db.org/network/9606.ENSG00000168884
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFZ5


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TNIP2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/TNIP2/TNIP2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000168884-TNIP2/subcellular

![](https://images.proteinatlas.org/49886/824_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/49886/824_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/49886/884_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/49886/884_H10_4_red_green.jpg)
![](https://images.proteinatlas.org/49886/978_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/49886/978_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NFZ5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR022008;IPR034735; |
| Pfam | PF12180; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168884-TNIP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IKBKG | Intact, Biogrid | true |
| MAP3K8 | Intact, Biogrid | true |
| NFKB1 | Intact, Biogrid | true |
| REL | Intact, Biogrid | true |
| STK11 | Intact, Biogrid | true |
| TNFAIP3 | Intact, Biogrid | true |
| ADRM1 | Biogrid | false |
| AMOT | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
