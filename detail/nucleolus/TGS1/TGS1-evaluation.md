---
type: protein-evaluation
gene: "TGS1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TGS1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TGS1 / PIMT |
| 蛋白全称 | Trimethylguanosine synthase |
| 蛋白大小 | 853 aa |
| UniProt ID | Q96RS0 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TGS1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TGS1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 8/10 | ×1 | **8** | 853 aa，尚可接受 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 63 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 2 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | PDB + AlphaFold 结构互证 (+0.5) |
|  | **原始总分** |  | **88.5/183** | **88.0/183** |  |  |  |
|  | **归一化总分** |  | **48.4/100** | **48.1/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Cytoplasm, Nucleus, Cajal body, Nucleus, nucleolus | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 853 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 63 |

**评价**: PubMed 63 篇，中等研究热度

**关键文献**:
1. Li C et al. (2026). "Targeting the ATM-TGS1-BRCA1 Axis Overcomes Genotoxic Therapy Resistance in Pancreatic Adenocarcinoma". *Cancer Res*. PMID: 41183146
2. Qiu X et al. (2025). "Integration of eQTL and multi-omics comprehensive analysis of triacylglycerol synthase 1 (TGS1) as a prognostic and immunotherapeutic biomarker across pan-cancer". *Int J Biol Macromol*. PMID: 39581398
3. Hayes KE et al. (2018). "Immunoprecipitation of Tri-methylated Capped RNA". *Bio Protoc*. PMID: 29527542
4. Kapadia B et al. (2023). "PIMT regulates hepatic gluconeogenesis in mice". *iScience*. PMID: 36866247
5. Challa NL et al. (2024). "TGS1/PIMT regulates pro-inflammatory macrophage mediated paracrine insulin resistance: Crosstalk between macrophages and skeletal muscle cells". *Biochim Biophys Acta Mol Basis Dis*. PMID: 37673359
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 853 aa |
| PDB 条数 | 2 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TGS1/TGS1-PAE.png]]

**评价**: 2 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | RNA_cap_Gua-N2-MeTrfase |
| InterPro | SAM-dependent_MTases_sf |
| Pfam | Methyltransf_15 |

**染色质调控潜力分析**: 3 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:small nuclear ribonucleoprotein complex (GO:0030532, IC:BHF-UCL)
- P:ribonucleoprotein complex biogenesis (GO:0022613, IC:BHF-UCL)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 2 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 63 篇，中等研究热度
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 2 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TGS1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137574-TGS1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TGS1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96RS0
- STRING: https://string-db.org/network/9606.ENSG00000137574
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RS0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TGS1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/TGS1/TGS1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000137574-TGS1/subcellular

![](https://images.proteinatlas.org/29824/777_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/29824/777_H2_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/29824/790_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29824/790_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29824/816_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29824/816_H2_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96RS0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019012;IPR029063; |
| Pfam | PF09445; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137574-TGS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBL | Intact, Biogrid, Opencell, Bioplex | true |
| SNRPB | Biogrid, Opencell | true |
| SNRPC | Biogrid, Opencell, Bioplex | true |
| SNRPF | Biogrid, Opencell | true |
| COIL | Biogrid | false |
| CREBBP | Biogrid | false |
| EED | Biogrid | false |
| EP300 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
