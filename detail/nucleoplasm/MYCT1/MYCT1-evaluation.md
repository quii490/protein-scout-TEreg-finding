---
type: protein-evaluation
gene: "MYCT1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYCT1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYCT1 / MTLC, MTMC1 |
| 蛋白大小 | 235 aa / 26.6 kDa |
| UniProt ID | [Q8N699](https://www.uniprot.org/uniprot/Q8N699) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus (UniProt), HPA: Nucleoplasm, GO: nuclear body, nucleoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 235 aa, 26.6 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed = 34 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | pLDDT = 60.56, PDB = 0 条目 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | Myc target 1 domain (PF15179) |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | No curated interactions |
| ➕ 互证加分 | — | max +3 | +0 | — |
| **原始总分** |  |  | **120/183** |  |
| **归一化总分** |  |  | **65.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus (UniProt), HPA: Nucleoplasm, GO: nuclear body, nucleoplasm | Experimental/ECO evidence |

**结论**: Nucleus (UniProt), HPA: Nucleoplasm, GO: nuclear body, nucleoplasm

#### 3.2 蛋白大小评估

235 aa (26.6 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 34 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- c-Myc target gene with HPA nucleoplasm confirmation. Very limited characterization. Function inferred from c-Myc regulation. No PPI data.

**关键文献**:
1. Xu J et al. (2023). "MYCT1 in cancer development: Gene structure, regulation, and biological implications." *Biomed Pharmacother*. PMID: 37499454
2. Lapitz A et al. (2023). "Liquid biopsy-based protein biomarkers for risk prediction, early diagnosis of cholangiocarcinoma." *J Hepatol*. PMID: 36868481
3. Fu S et al. (2011). "MYCT1-TV, a novel MYCT1 transcript, is regulated by c-Myc." *PLoS One*. PMID: 21998677
4. Dong X et al. (2024). "MYCT-1 Gene Expression in Patients with Gastric Cancer." *Appl Biochem Biotechnol*. PMID: 38112991
5. Chen J et al. (2025). "Integrative Analysis of Endothelial Cell Senescence-Related Genes in IPF." *FASEB J*. PMID: 41351492

**评价**: c-Myc target gene with HPA nucleoplasm confirmation. Very limited characterization. Function inferred from c-Myc regulation. No PPI data.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 60.56 |
| 有序区域 (pLDDT>70) 占比 | 34.0% |
| 可用 PDB 条目 | 0 个 (—) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYCT1/MYCT1-PAE.png]]

**评价**: Target of c-Myc transcription factor. MYCT1 is regulated by c-Myc and may participate in c-Myc-mediated transcriptional programs.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | Myc target 1 domain (PF15179) |

**染色质调控潜力分析**: Target of c-Myc transcription factor. MYCT1 is regulated by c-Myc and may participate in c-Myc-mediated transcriptional programs.

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
- GO: nuclear body, nucleoplasm

**IntAct 查询记录**: IntAct 查询无物理互作记录

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: c-Myc target gene with HPA nucleoplasm confirmation. Very limited characterization. Function inferred from c-Myc regulation. No PPI data.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=60.56, PDB=0条目 | — |
| 结构域 | UniProt / InterPro / Pfam | Myc target 1 domain (PF15179) | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus (UniProt), HPA: Nucleoplasm, GO: nuclear body, nucle | — |

**互证加分明细**:
- —
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. HPA Nucleoplasm confirmation
2. c-Myc target gene (transcriptional link)
3. Reasonable novelty (PubMed=34)
4. Good size (235aa)

**风险/不确定性**:
1. Very limited functional characterization
2. No structural domains beyond MYCT1 family
3. No PPI data at all
4. AlphaFold moderate-low (pLDDT 60.6)
5. No PDB structures
6. Function only inferred from c-Myc regulation

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q8N699
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N699
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYCT1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q8N699


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MYCT1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MYCT1/MYCT1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000120279-MYCT1/subcellular

![](https://images.proteinatlas.org/47992/1000_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/47992/1000_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/47992/1003_G10_3_red_green.jpg)
![](https://images.proteinatlas.org/47992/1003_G10_4_red_green.jpg)
![](https://images.proteinatlas.org/47992/2154_D4_3_red_green.jpg)
![](https://images.proteinatlas.org/47992/2154_D4_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
