---
type: protein-evaluation
gene: "NIP7"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NIP7 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NIP7 / CGI-37|FLJ10296|HSPC031|KD93 |
| 蛋白名称 | 60S ribosome subunit biogenesis protein NIP7 homolog |
| 蛋白大小 | 180 aa |
| UniProt ID | Q9Y221 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NIP7/IF_images/CACO-2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NIP7/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | **24** | 核+胞质，有核定位证据 |
| 📏 蛋白大小 | 8/10 | ×1 | **8** | 180 aa，可接受范围 |
| 🆕 研究新颖性 | 10/10 | ×5 | **50** | PubMed 15篇，极度新颖 |
| 🏗️ 三维结构 | 10/10 | ×3 | **30** | 8 个 PDB 实验结构，实验验证充分 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 11 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.5** | 三维结构: AlphaFold + PDB 双源 (+0.5); PPI: IntAct + STRING 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
| **原始总分** |  |  | **138.5/183** |  |
| **归一化总分** |  |  | **75.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | N/A | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |

**结论**: 核+胞质，有核定位证据

#### 3.2 蛋白大小评估

**评价**: 180 aa，180 aa，可接受范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 15 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 4.2587 |

**关键文献**:
1. Zanchin et al. (1997). "Saccharomyces cerevisiae Nip7p is required for efficient 60S ribosome subunit biogenesis.". *Mol Cell Biol*. PMID: 9271378
2. Gutierrez et al. (2024). "Assigning roles in Chlamydomonas ribosome biogenesis: The conserved factor NIP7.". *Biochim Biophys Acta Proteins Proteom*. PMID: 39216654
3. Routray et al. (2018). "Nodulin Intrinsic Protein 7;1 Is a Tapetal Boric Acid Channel Involved in Pollen Cell Wall Formation.". *Plant Physiol*. PMID: 30266747
4. Wei et al. (2025). "Mendelian randomization provides a multi-omics perspective on the regulation of genes involved in ribosome biogenesis in relation to cardiac structure and function.". *Clin Epigenetics*. PMID: 40045424
5. Gong et al. (2025). "[NIP7 upregulates the expression of ubiquitin-conjugating enzyme E2 C to promote tumor growth in anaplastic thyroid cancer].". *Zhejiang Da Xue Xue Bao Yi Xue Ban*. PMID: 40461291
**评价**: PubMed 15篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 180 aa |
| PDB 条目数 | 8 |
| UniProt 注释结构域数 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NIP7/NIP7-PAE.png]]

**评价**: 8 个 PDB 实验结构，实验验证充分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | NIP7_N |
| InterPro | Nip7_N_euk |
| InterPro | PUA |
| InterPro | PUA-like_sf |
| InterPro | PUA_sf |
| InterPro | Ribosomal_synth_fac_NIP7 |
| InterPro | UPF0113_PUA |
| Pfam | pre-PUA_NIP7 |
| Pfam | UPF0113 |
| SMART | PUA |
| PROSITE | PUA |

**染色质调控潜力分析**: 11 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 226 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| BRIX1 | 0 |  | 否 |
| WDR12 | 0 |  | 否 |
| EBNA1BP2 | 0 |  | 否 |
| NIFK | 0 |  | 否 |
| MRTO4 | 0 |  | 否 |
| RSL24D1 | 0 |  | 否 |
| RPF1 | 0 |  | 否 |
| NOP2 | 0 |  | 否 |
| NSA2 | 0 |  | 否 |
| GTPBP4 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 8 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 11 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 226 IntAct | 双源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
三维结构: AlphaFold + PDB 双源 (+0.5)
PPI: IntAct + STRING 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 15 篇，极度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 8 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NIP7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132603-NIP7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NIP7%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y221
- STRING: https://string-db.org/network/9606.ENSG00000132603
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y221


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NIP7-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NIP7/NIP7-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y221 |
| SMART | SM00359; |
| UniProt Domain [FT] | DOMAIN 94..170; /note="PUA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00161" |
| InterPro | IPR040598;IPR055359;IPR002478;IPR015947;IPR036974;IPR016686;IPR005155; |
| Pfam | PF17833;PF03657; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132603-NIP7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NOP2 | Intact, Biogrid | true |
| ANLN | Biogrid | false |
| CRX | Intact | false |
| DDX24 | Biogrid | false |
| LZTS2 | Intact | false |
| NOL8 | Biogrid | false |
| OPTN | Intact | false |
| RBM28 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
