---
type: protein-evaluation
gene: "MEAF6"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEAF6 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEAF6 / C1orf149, CENP-28, EAF6 |
| 蛋白大小 | 191 aa / 21.6 kDa |
| UniProt ID | [Q9HAF1](https://www.uniprot.org/uniprot/Q9HAF1) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus/Nucleolus/Kinetochore (UniProt), GO: NuA4 HAT, MOZ/MORF HAT, nucleolus, |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 191 aa, 21.6 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed = 28 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | pLDDT = 70.88, PDB = 0 条目 |
| 🧬 调控结构域 | 10/10 | ×2 | 20 | Eaf6 domain (PF09340) |
| 🔗 PPI 网络 | 10/10 | ×3 | 30 | BYSL, C2CD6, ELAVL4, FGFR3, FXR2, HTT, JADE2, L3MBTL2, LDOC1 |
| ➕ 互证加分 | — | max +3 | +2 | — |
| **原始总分** |  |  | **150/183** |  |
| **归一化总分** |  |  | **82.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis），核定位基于 UniProt + GO（多项组蛋白乙酰转移酶复合体注释） | — |
| UniProt | Nucleus/Nucleolus/Kinetochore (UniProt), GO: NuA4 HAT, MOZ/MORF HAT, nucleolus, nucleoplasm, nucleos | Experimental/ECO evidence |

**结论**: Nucleus/Nucleolus/Kinetochore (UniProt), GO: NuA4 HAT, MOZ/MORF HAT, nucleolus, nucleoplasm, nucleosome, nucleus

#### 3.2 蛋白大小评估

191 aa (21.6 kDa)，在理想生化实验范围（200-800 aa）外。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 28 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- Core subunit of NuA4/Tip60 and MOZ/MORF histone acetyltransferase complexes. Direct histone modification. Extremely high-confidence PPI (STRING >0.99) with chromatin modifiers.

**关键文献**:
1. Su Z et al. (2024). "Multifunctional acyltransferase HBO1: a key regulatory factor for cellular functions." *Cell Mol Biol Lett*. PMID: 39543485
2. Zu G et al. (2022). "BRPF1-KAT6A/KAT6B Complex: Molecular Structure, Biological Function and Human Disease." *Cancers (Basel)*. PMID: 36077605
3. Lee AR et al. (2017). "Alternative RNA splicing of the MEAF6 gene facilitates neuroendocrine prostate cancer progression." *Oncotarget*. PMID: 28427194
4. Bai W et al. (2022). "Protein succinylation associated with the progress of hepatocellular carcinoma." *J Cell Mol Med*. PMID: 36308411
5. Schneider N et al. (2016). "Ossifying fibromyxoid tumor: morphology, genetics, and differential diagnosis." *Ann Diagn Pathol*. PMID: 26732302

**评价**: Core subunit of NuA4/Tip60 and MOZ/MORF histone acetyltransferase complexes. Direct histone modification. Extremely high-confidence PPI (STRING >0.99) with chromatin modifiers.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 70.88 |
| 有序区域 (pLDDT>70) 占比 | 42.4% |
| 可用 PDB 条目 | 0 个 (—) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEAF6/MEAF6-PAE.png]]

**评价**: Core subunit of NuA4/Tip60 and MOZ/MORF histone acetyltransferase (HAT) complexes. Direct role in histone modification and chromatin regulation.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | Eaf6 domain (PF09340) |

**染色质调控潜力分析**: Core subunit of NuA4/Tip60 and MOZ/MORF histone acetyltransferase (HAT) complexes. Direct role in histone modification and chromatin regulation.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| BYSL, C2CD6, ELAVL4, FGFR3, FXR2, HTT, JADE2, L3MBTL2, LDOC1 | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| EPC1(0.999), TRRAP(0.999), YEATS4(0.999), ING4(0.999), KAT5(0.999), KAT7(0.999), | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: histone acetyltransferase complex, MOZ/MORF HAT complex, NuA4 HAT complex, nucleolus, nucleoplasm, nucleosome, nucleus

**IntAct 查询记录**: IntAct: 大量 NuA4 复合体成员物理互作

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: Core subunit of NuA4/Tip60 and MOZ/MORF histone acetyltransferase complexes. Direct histone modification. Extremely high-confidence PPI (STRING >0.99) with chromatin modifiers.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=70.88, PDB=0条目 | — |
| 结构域 | UniProt / InterPro / Pfam | Eaf6 domain (PF09340) | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus/Nucleolus/Kinetochore (UniProt), GO: NuA4 HAT, MOZ/M | — |

**互证加分明细**:
- —
**总分**: +2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. Subunit of NuA4 + MOZ/MORF HAT complexes
2. Extremely high-confidence PPI with KAT5/KAT6/KAT7 acetyltransferases
3. Direct chromatin modification function
4. Novel (PubMed=28)
5. 8 GO-CC chromatin complex annotations

**风险/不确定性**:
1. Small protein (191aa, size score 8)
2. AlphaFold moderate-low (pLDDT 70.9, 42.4% ordered)
3. No PDB structures
4. Functions as part of large complexes

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q9HAF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HAF1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEAF6%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q9HAF1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MEAF6-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEAF6/MEAF6-PAE.png]]
