---
type: protein-evaluation
gene: "MEIKIN"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEIKIN 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEIKIN /  |
| 蛋白大小 | 373 aa / 40.8 kDa |
| UniProt ID | [A0A087WXM9](https://www.uniprot.org/uniprot/A0A087WXM9) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | Chromosome centromere/kinetochore (UniProt), GO: condensed chromosome centromeri |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 373 aa, 40.8 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed = 5 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | pLDDT = 53.94, PDB = 0 条目 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | Meikin domain (no Pfam) |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | No curated interactions |
| ➕ 互证加分 | — | max +3 | +0 | — |
| **原始总分** |  |  | **126/183** |  |
| **归一化总分** |  |  | **68.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis），核定位基于 UniProt + GO（centromere/kinetochore） | — |
| UniProt | Chromosome centromere/kinetochore (UniProt), GO: condensed chromosome centromeric region, kinetochor | Experimental/ECO evidence |

**结论**: Chromosome centromere/kinetochore (UniProt), GO: condensed chromosome centromeric region, kinetochore

#### 3.2 蛋白大小评估

373 aa (40.8 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 5 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- Meiosis-specific kinetochore protein. Extremely novel (PubMed=5) but function is specific to meiotic chromosome segregation. Not chromatin/transcription.

**关键文献**:
1. Maier NK et al. (2021). "Separase cleaves the kinetochore protein Meikin at the meiosis I/II transition." *Dev Cell*. PMID: 34331869
2. Liu Y et al. (2024). "Phosphorylation of Rec8 cohesin complexes regulates mono-orientation of kinetochores in meiosis I." *Life Sci Alliance*. PMID: 38448160
3. Fan LH et al. (2024). "MEIKIN expression and its C-terminal phosphorylation by PLK1 is closely related the metaphase-anaphase transition." *Histochem Cell Biol*. PMID: 39093409
4. Miyazaki S et al. (2017). "Meikin-associated polo-like kinase specifies Bub1 distribution in meiosis I." *Genes Cells*. PMID: 28497540
5. Galander S et al. (2019). "Spo13 prevents premature cohesin cleavage during meiosis." *Wellcome Open Res*. PMID: 30906881

**评价**: Meiosis-specific kinetochore protein. Extremely novel (PubMed=5) but function is specific to meiotic chromosome segregation. Not chromatin/transcription.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 53.94 |
| 有序区域 (pLDDT>70) 占比 | 7.2% |
| 可用 PDB 条目 | 0 个 (—) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEIKIN/MEIKIN-PAE.png]]

**评价**: Meiosis-specific kinetochore factor. Regulates mono-orientation of sister kinetochores in meiosis I. Substrate of separase and PLK1.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | Meikin domain (no Pfam) |

**染色质调控潜力分析**: Meiosis-specific kinetochore factor. Regulates mono-orientation of sister kinetochores in meiosis I. Substrate of separase and PLK1.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| No curated interactions | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| STRING 数据不可用 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: condensed chromosome centromeric region, kinetochore

**IntAct 查询记录**: IntAct 查询无物理互作记录

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: Meiosis-specific kinetochore protein. Extremely novel (PubMed=5) but function is specific to meiotic chromosome segregation. Not chromatin/transcription.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=53.94, PDB=0条目 | — |
| 结构域 | UniProt / InterPro / Pfam | Meikin domain (no Pfam) | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Chromosome centromere/kinetochore (UniProt), GO: condensed c | — |

**互证加分明细**:
- —
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. Ultra-novel (PubMed=5)
2. Meiosis-specific - poorly understood niche
3. Chromosomal centromere/kinetochore localization

**风险/不确定性**:
1. Meiosis-specific - not relevant outside germ cells
2. Very poor structural quality (pLDDT 53.9)
3. No PDB structures
4. No PPI data
5. No chromatin/transcription function

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/A0A087WXM9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A087WXM9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEIKIN%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/A0A087WXM9


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MEIKIN-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEIKIN/MEIKIN-PAE.png]]
