---
type: protein-evaluation
gene: "MYEF2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYEF2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYEF2 / KIAA1341 |
| 蛋白大小 | 600 aa / 64.1 kDa |
| UniProt ID | [Q9P2K5](https://www.uniprot.org/uniprot/Q9P2K5) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus (UniProt), HPA: Nucleoplasm, GO: nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 600 aa, 64.1 kDa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed = 96 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | pLDDT = 61.12, PDB = 0 条目 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | RRM domain (PF00076) - 3 copies |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | No curated interactions |
| ➕ 互证加分 | — | max +3 | +0 | — |
| **原始总分** |  |  | **98/183** |  |
| **归一化总分** |  |  | **53.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus (UniProt), HPA: Nucleoplasm, GO: nucleus | Experimental/ECO evidence |

**结论**: Nucleus (UniProt), HPA: Nucleoplasm, GO: nucleus

#### 3.2 蛋白大小评估

600 aa (64.1 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 96 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- RNA-binding protein with 3 RRM domains. Regulates myelin gene expression. STRING shows spliceosome/RNA processing partners. HPA Nucleoplasm.

**关键文献**:
1. Zhang P et al. (2023). "Expression and function of myelin expression factor 2 in hepatocellular carcinoma." *BMC Gastroenterol*. PMID: 36658471
2. Zhang Y et al. (2023). "MYEF2: an immune infiltration-related prognostic factor in IDH-wild-type glioblastoma." *Aging (Albany NY)*. PMID: 37556355
3. Johnston WL et al. (2017). "C. elegans SUP-46, an HNRNPM family RNA-binding protein." *BMC Biol*. PMID: 28716093
4. Xin R et al. (2025). "Non-Coding RNAs as Robust Plasma Biomarkers of Alzheimer's Disease." *Biomolecules*. PMID: 40563446
5. Lei J et al. (2024). "eEF1A1 regulates the expression and alternative splicing of genes associated with Parkinson's disease." *Genes Genomics*. PMID: 38776049

**评价**: RNA-binding protein with 3 RRM domains. Regulates myelin gene expression. STRING shows spliceosome/RNA processing partners. HPA Nucleoplasm.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 61.12 |
| 有序区域 (pLDDT>70) 占比 | 38.2% |
| 可用 PDB 条目 | 0 个 (—) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYEF2/MYEF2-PAE.png]]

**评价**: Three RNA recognition motifs (RRMs). RNA-binding protein regulating myelin gene expression. HNRNPM family. Alternative splicing regulation.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | RRM domain (PF00076) - 3 copies |

**染色质调控潜力分析**: Three RNA recognition motifs (RRMs). RNA-binding protein regulating myelin gene expression. HNRNPM family. Alternative splicing regulation.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| No curated interactions | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CTXN2(0.751), XAB2(0.734), HNRNPM(0.682), SOX2(0.682), CRNKL1(0.677), SYF2(0.676 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: nucleus

**IntAct 查询记录**: IntAct 查询无物理互作记录

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: RNA-binding protein with 3 RRM domains. Regulates myelin gene expression. STRING shows spliceosome/RNA processing partners. HPA Nucleoplasm.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=61.12, PDB=0条目 | — |
| 结构域 | UniProt / InterPro / Pfam | RRM domain (PF00076) - 3 copies | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus (UniProt), HPA: Nucleoplasm, GO: nucleus | — |

**互证加分明细**:
- —
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 3 RRM domains - RNA binding with structural basis
2. HPA Nucleoplasm confirmation
3. RNA processing/splicing role
4. Spliceosome partner associations

**风险/不确定性**:
1. Moderate-low novelty (PubMed=96)
2. RNA binding, not chromatin/DNA
3. No PDB structures
4. AlphaFold moderate-low (pLDDT 61.1)
5. Limited PPI

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q9P2K5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2K5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYEF2%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q9P2K5


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MYEF2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYEF2/MYEF2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000104177-MYEF2/subcellular

![](https://images.proteinatlas.org/4883/2269_B3_38_red_green.jpg)
![](https://images.proteinatlas.org/4883/2269_B3_88_red_green.jpg)
![](https://images.proteinatlas.org/4883/68_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/4883/68_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/4883/69_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/4883/69_D3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
