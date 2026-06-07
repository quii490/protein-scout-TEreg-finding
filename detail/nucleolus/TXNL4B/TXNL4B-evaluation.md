---
type: protein-evaluation
gene: "TXNL4B"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TXNL4B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TXNL4B / FLJ20511|DLP|Dim2 |
| 蛋白全称 | Thioredoxin-like protein 4B |
| 蛋白大小 | 149 aa |
| UniProt ID | Q9NX01 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TXNL4B/IF_images/CACO-2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TXNL4B/IF_images/HEK293_1.jpg|HEK293]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 149 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 24 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 4 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5) |
| **原始总分** |  |  | **125/183** |  |
| **归一化总分** |  |  | **68.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 149 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 24 |

**评价**: PubMed 24 篇，高度新颖

**关键文献**:
1. Bai R et al. (2024). "Structural basis of U12-type intron engagement by the fully assembled human minor spliceosome". *Science*. PMID: 38484052
2. Hong Y (2026). "Uncovering novel protein pathways regulating bioavailable testosterone through sex hormone-binding globulin". *Comput Biol Chem*. PMID: 41161126
3. Li M et al. (2024). "Identification of susceptibility loci and relevant cell type for IgA nephropathy in Han Chinese by integrative genome-wide analysis". *Front Med*. PMID: 39343836
4. Jin T et al. (2013). "High-resolution crystal structure of human Dim2/TXNL4B". *Acta Crystallogr Sect F Struct Biol Cryst Commun*. PMID: 23519793
5. Ju Z et al. (2023). "TXNL4B regulates radioresistance by controlling the PRP3-mediated alternative splicing of FANCI". *MedComm (2020)*. PMID: 37168687
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 149 aa |
| PDB 条数 | 4 |
| 已注释结构域 | 4 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TXNL4B/TXNL4B-PAE.png]]

**评价**: 4 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Dim1 |
| InterPro | Thioredoxin-like_sf |
| Pfam | DIM1 |
| SMART | DIM1 |

**染色质调控潜力分析**: 4 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:spliceosomal complex (GO:0005681, IBA:GO_Central)
- C:U4/U6 x U5 tri-snRNP complex (GO:0046540, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 4 条 | 一致 |
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
1. 新颖性: PubMed 24 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 4 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TXNL4B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140830-TXNL4B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TXNL4B%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9NX01
- STRING: https://string-db.org/network/9606.ENSG00000140830
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NX01


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TXNL4B-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/TXNL4B/TXNL4B-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000140830-TXNL4B/subcellular

![](https://images.proteinatlas.org/65865/1249_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/65865/1249_B12_5_red_green.jpg)
![](https://images.proteinatlas.org/65865/1258_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/65865/1258_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/65865/1284_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/65865/1284_H4_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NX01 |
| SMART | SM01410; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004123;IPR036249; |
| Pfam | PF02966; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140830-TXNL4B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CENATAC | Intact, Biogrid, Bioplex | true |
| AIPL1 | Intact | false |
| ALKBH4 | Intact | false |
| BHLHE40 | Intact | false |
| FCGRT | Bioplex | false |
| MEOX1 | Intact | false |
| PICK1 | Intact | false |
| PLEKHF2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
