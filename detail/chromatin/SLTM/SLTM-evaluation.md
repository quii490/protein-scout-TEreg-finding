---
type: protein-evaluation
gene: "SLTM"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SLTM 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SLTM / Met|FLJ13213 |
| 蛋白全称 | SAFB-like transcription modulator |
| 蛋白大小 | 1034 aa |
| UniProt ID | Q9NWH9 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SLTM/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SLTM/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 1034 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 30 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 12 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **119/183** |  |
| **归一化总分** |  |  | **65.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 1034 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 30 |

**关键文献**:
1. Kaisinger et al. (2023). "Large-scale exome sequence analysis identifies sex- and age-specific determinants of obesity.". *Cell Genom*. PMID: 37601970
2. Banerjee et al. (2025). "Discovery of obesity genes through cross-ancestry analysis.". *Nat Commun*. PMID: 41168175
3. Hong et al. (2025). "Integrative causal and single-cell analyses reveal genes responsive to endocrine disruptors driving human male infertility.". *Ecotoxicol Environ Saf*. PMID: 40700968
4. Chen et al. (2024). "Hypoxia-induced DTL promotes the proliferation, metastasis, and sorafenib resistance of hepatocellular carcinoma through ubiquitin-mediated degradation of SLTM and subsequent Notch pathway activation.". *Cell Death Dis*. PMID: 39384740
5. Blokland et al. (2022). "Sex-Dependent Shared and Nonshared Genetic Architecture Across Mood and Psychotic Disorders.". *Biol Psychiatry*. PMID: 34099189
**评价**: PubMed 30 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1034 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 12 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SLTM/SLTM-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Nucleotide-bd_a/b_plait_sf |
| InterPro | RBD_domain_sf |
| InterPro | RRM_dom |
| InterPro | SAF_Modulators |
| InterPro | SAP_dom |
| InterPro | SAP_dom_sf |
| Pfam | RRM_1 |
| Pfam | SAP |
| SMART | RRM |
| SMART | SAP |
| PROSITE | RRM |
| PROSITE | SAP |

**染色质调控潜力分析**: 12 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 12 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 30 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SLTM
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137776-SLTM
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SLTM%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9NWH9
- STRING: https://string-db.org/network/9606.ENSG00000137776
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWH9


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SLTM-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SLTM/SLTM-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000137776-SLTM/subcellular

![](https://images.proteinatlas.org/40256/411_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/40256/411_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/40256/415_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/40256/415_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/40256/416_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/40256/416_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NWH9 |
| SMART | SM00360;SM00513; |
| UniProt Domain [FT] | DOMAIN 22..56; /note="SAP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00186"; DOMAIN 384..462; /note="RRM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176" |
| InterPro | IPR012677;IPR035979;IPR000504;IPR051738;IPR003034;IPR036361; |
| Pfam | PF00076;PF02037; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137776-SLTM/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CEP19 | Biogrid, Bioplex | true |
| ANLN | Biogrid | false |
| ARL13B | Bioplex | false |
| CCDC70 | Bioplex | false |
| CPSF6 | Opencell | false |
| DDX21 | Opencell | false |
| ERLEC1 | Bioplex | false |
| EXOSC4 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
