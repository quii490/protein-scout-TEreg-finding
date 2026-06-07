---
type: protein-evaluation
gene: "NUFIP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NUFIP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NUFIP1 / NUFIP|Rsa1 |
| 蛋白名称 | FMR1-interacting protein NUFIP1 |
| 蛋白大小 | 495 aa |
| UniProt ID | Q9UHK0 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NUFIP1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NUFIP1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 495 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 74篇，有一定研究空间 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 10/10 | ×2 | **20** | 明确染色质/DNA 调控结构域: zinc_finger_c2h2_1, zinc_finger_c2h2_2, znf_c2h2, znf_c2h2_type |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+2.0** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
|  | **原始总分** |  | **119/183** | **118.0/183** |  |
|  | **归一化总分** |  | **65.0/100** | **64.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 495 aa，495 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 74 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 5.0886 |

**关键文献**:
1. Wyant et al. (2018). "NUFIP1 is a ribosome receptor for starvation-induced ribophagy.". *Science*. PMID: 29700228
2. Chen et al. (2025). "Rpl12 is a conserved ribophagy receptor.". *Nat Cell Biol*. PMID: 39934334
3. Yao et al. (2021). "Organelle-specific autophagy in inflammatory diseases: a potential therapeutic target underlying the quality control of multiple organelles.". *Autophagy*. PMID: 32048886
4. Ming et al. (2025). "NUFIP1 integrates amino acid sensing and DNA damage response to maintain the intestinal homeostasis.". *Nat Metab*. PMID: 39753713
5. Jin et al. (2018). "Finding a ribophagy receptor.". *Autophagy*. PMID: 30067425
**评价**: PubMed 74篇，有一定研究空间

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 495 aa |
| PDB 条目数 | 1 |
| UniProt 注释结构域数 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NUFIP1/NUFIP1-PAE.png]]

**评价**: 1 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | NUFIP1-like |
| InterPro | NUFIP1_cons_dom |
| InterPro | Znf_C2H2_type |
| Pfam | NUFIP1 |
| SMART | ZnF_C2H2 |
| PROSITE | ZINC_FINGER_C2H2_1 |
| PROSITE | ZINC_FINGER_C2H2_2 |

**染色质调控潜力分析**: 明确染色质/DNA 调控结构域: zinc_finger_c2h2_1, zinc_finger_c2h2_2, znf_c2h2, znf_c2h2_type

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ZNHIT3 | 0 |  | 否 |
| ZNHIT6 | 0 |  | 否 |
| NOP58 | 0 |  | 否 |
| FMR1 | 0 |  | 否 |
| SNU13 | 0 |  | 否 |
| FXR1 | 0 |  | 否 |
| PIH1D1 | 0 |  | 否 |
| NUFIP2 | 0 |  | 否 |
| FXR2 | 0 |  | 否 |
| NOP56 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- C:perichromatin fibrils (GO:0005726, IDA:HGNC-UCL)
- C:pre-snoRNP complex (GO:0070761, IDA:BHF-UCL)
- C:protein-containing complex (GO:0032991, IDA:BHF-UCL)
- C:transcription elongation factor complex (GO:0008023, IDA:HGNC-UCL)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 7 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 74 篇，有一定研究空间
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 1 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NUFIP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000083635-NUFIP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NUFIP1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9UHK0
- STRING: https://string-db.org/network/9606.ENSG00000083635
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHK0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NUFIP1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NUFIP1/NUFIP1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UHK0 |
| SMART | SM00355; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039136;IPR019496;IPR013087; |
| Pfam | PF10453; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000083635-NUFIP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NOP58 | Biogrid, Opencell | true |
| RUVBL1 | Biogrid, Bioplex | true |
| RUVBL2 | Biogrid, Opencell | true |
| SNU13 | Intact, Biogrid | true |
| ZNHIT3 | Intact, Biogrid, Bioplex | true |
| ZNHIT6 | Intact, Biogrid, Bioplex | true |
| BRCA1 | Biogrid | false |
| CCNT1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
