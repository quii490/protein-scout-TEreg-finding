---
type: protein-evaluation
gene: "METTL5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## METTL5 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | METTL5 /  |
| 蛋白大小 | 209 aa / 23.7 kDa |
| UniProt ID | [Q9NRN9](https://www.uniprot.org/uniprot/Q9NRN9) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus (UniProt), GO: nucleolus, nucleus, fibrillar center |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 209 aa, 23.7 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed = 51 篇 |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | pLDDT = 92.62, PDB = 3 条目 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | rRNA methyltransferase (PF05175), SAM-dependent MTase superfamily |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | TRMT112, ZBTB5 |
| ➕ 互证加分 | — | max +3 | +0 | — |
| **原始总分** |  |  | **126/183** |  |
| **归一化总分** |  |  | **68.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus (UniProt), GO: nucleolus, nucleus, fibrillar center | Experimental/ECO evidence |

**结论**: Nucleus (UniProt), GO: nucleolus, nucleus, fibrillar center

#### 3.2 蛋白大小评估

209 aa (23.7 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 51 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- rRNA m6A methyltransferase with excellent structural data (3 PDB, pLDDT 92.6). Specific 18S rRNA modifier. Well-characterized enzymatic function.

**关键文献**:
1. Peng H et al. (2022). "N6-methyladenosine (m6A) in 18S rRNA promotes fatty acid metabolism and oncogenic transformation." *Nat Metab*. PMID: 35999469
2. Sendinc E et al. (2023). "RNA m6A methylation across the transcriptome." *Mol Cell*. PMID: 36736310
3. Xia P et al. (2023). "METTL5 stabilizes c-Myc by facilitating USP5 translation." *Cancer Commun (Lond)*. PMID: 36602428
4. Qi YN et al. (2023). "Methyltransferase-like proteins in cancer biology." *J Hematol Oncol*. PMID: 37533128
5. Zhang M et al. (2025). "METTL5 deficiency induces oligoasthenoteratozoospermia." *Mol Ther*. PMID: 40783785

**评价**: rRNA m6A methyltransferase with excellent structural data (3 PDB, pLDDT 92.6). Specific 18S rRNA modifier. Well-characterized enzymatic function.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 92.62 |
| 有序区域 (pLDDT>70) 占比 | 93.7% |
| 可用 PDB 条目 | 3 个 (6H2U, 6H2V, 9OHL) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL5/METTL5-PAE.png]]

**评价**: rRNA N6-adenosine methyltransferase responsible for m6A modification of 18S rRNA. SAM-dependent methyltransferase. Well-characterized enzymatic mechanism.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | rRNA methyltransferase (PF05175), SAM-dependent MTase superfamily |

**染色质调控潜力分析**: rRNA N6-adenosine methyltransferase responsible for m6A modification of 18S rRNA. SAM-dependent methyltransferase. Well-characterized enzymatic mechanism.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| TRMT112, ZBTB5 | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| STRING 数据不可用 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: cytosol, fibrillar center, nucleolus, nucleus, postsynapse, presynapse

**IntAct 查询记录**: IntAct: TRMT112 (co-factor) 物理互作

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: rRNA m6A methyltransferase with excellent structural data (3 PDB, pLDDT 92.6). Specific 18S rRNA modifier. Well-characterized enzymatic function.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=92.62, PDB=3条目 | — |
| 结构域 | UniProt / InterPro / Pfam | rRNA methyltransferase (PF05175), SAM-dependent MTase superf | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus (UniProt), GO: nucleolus, nucleus, fibrillar center | — |

**互证加分明细**:
- —
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. Excellent structural data (3 PDB + pLDDT 92.6)
2. Clear enzymatic function (rRNA m6A methyltransferase)
3. Nuclear/nucleolar localization

**风险/不确定性**:
1. Not chromatin/DNA-related (rRNA modification)
2. Moderate novelty (PubMed=51)
3. Small protein (209aa)
4. Limited PPI

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q9NRN9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRN9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=METTL5%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q9NRN9


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[METTL5-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL5/METTL5-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000138382-METTL5/subcellular

![](https://images.proteinatlas.org/38223/431_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38223/431_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38223/437_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38223/437_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38223/443_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38223/443_C11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
