---
type: protein-evaluation
gene: "SSBP3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SSBP3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SSBP3 / CSDP|SSDP|FLJ10355|SSDP1 |
| 蛋白全称 | Single-stranded DNA-binding protein 3 |
| 蛋白大小 | 388 aa |
| UniProt ID | Q9BWW4 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SSBP3/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 388 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 29 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 5 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **121/183** |  |
| **归一化总分** |  |  | **66.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 388 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 29 |

**评价**: PubMed 29 篇，高度新颖

**关键文献**:
1. Wang X et al. (2025). "Single-stranded DNA-binding proteins are essential components of the architectural LDB1 protein complex". *Mol Cell*. PMID: 40803327
2. Wang X et al. (2025). "Single-stranded DNA binding proteins are essential components of the architectural LDB1 protein complex". *bioRxiv*. PMID: 40502025
3. Yin Z et al. (2018). "[SIVA1 Regulates the Stability of Single-Stranded DNA-Binding Protein 3 Isoforms]". *Mol Biol (Mosk)*. PMID: 30363057
4. Toren E et al. (2023). "The SSBP3 co-regulator is required for glucose homeostasis, pancreatic islet architecture, and beta-cell identity". *Mol Metab*. PMID: 37536498
5. Choi MR et al. (2018). "Possible Role of Single Stranded DNA Binding Protein 3 on Skin Hydration by Regulating Epidermal Differentiation". *Ann Dermatol*. PMID: 30065583
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 388 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 5 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SSBP3/SSBP3-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | LisH |
| InterPro | SSDP_DNA-bd |
| Pfam | SSDP |
| SMART | LisH |
| PROSITE | LISH |

**染色质调控潜力分析**: 5 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| IL36RN | two hybrid array | 32296183 | — | — |
| LDB1 | two hybrid array | 25416956 | — | — |
| DTNB | validated two hybrid | 32296183 | — | — |
| SS18L1 | validated two hybrid | 32296183 | — | — |
| BLK | two hybrid array | 32296183 | — | — |
| PIN1 | two hybrid array | 32296183 | — | — |
| NXT2 | validated two hybrid | 32296183 | — | — |
| YES1 | validated two hybrid | 32296183 | — | — |
| ARNT2 | two hybrid array | 24722188 | — | — |
| EWSR1 | validated two hybrid | 25416956 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:transcription regulator complex (GO:0005667, IEA:Ensembl)
- P:protein-containing complex assembly (GO:0065003, IEA:Ensembl)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 5 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 29 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SSBP3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157216-SSBP3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SSBP3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9BWW4
- STRING: https://string-db.org/network/9606.ENSG00000157216
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWW4


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SSBP3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/SSBP3/SSBP3-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000157216-SSBP3/subcellular

![](https://images.proteinatlas.org/71780/1776_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/71780/1776_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BWW4 |
| SMART | SM00667; |
| UniProt Domain [FT] | DOMAIN 16..48; /note="LisH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00126" |
| InterPro | IPR006594;IPR008116; |
| Pfam | PF04503; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157216-SSBP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LDB1 | Intact, Biogrid | true |
| LMX1B | Intact, Biogrid | true |
| BLK | Intact | false |
| EWSR1 | Intact | false |
| IL36RN | Intact | false |
| ISL1 | Biogrid | false |
| ISL2 | Biogrid | false |
| LDB2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
