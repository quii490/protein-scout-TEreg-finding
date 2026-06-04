---
type: protein-evaluation
gene: "MFAP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MFAP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MFAP1 /  |
| 蛋白大小 | 439 aa / 52.0 kDa |
| UniProt ID | [P55081](https://www.uniprot.org/uniprot/P55081) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/MFAP1/IF_images/SiHa_1.jpg|SiHa]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/MFAP1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus (UniProt), HPA: Nucleoli , Nucleoli fibrillar center, GO: nucleoplasm, nuc |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 439 aa, 52.0 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed = 11 篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | pLDDT = 71.31, PDB = 12 条目 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | MFAP1 domain (PF06991) |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 |ALKBH8, AMOTL2, AP2M1, BEND7, BICD2, BLZF1, CARD9, CDC14B, C |
| ➕ 互证加分 | — | max +3 | +1 | — |
| **原始总分** |  |  | **149/183** |  |
| **归一化总分** |  |  | **81.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus (UniProt), HPA: Nucleoli|Nucleoli fibrillar center, GO: nucleoplasm, nucleus, U2-type splice | Experimental/ECO evidence |

**结论**: Nucleus (UniProt), HPA: Nucleoli|Nucleoli fibrillar center, GO: nucleoplasm, nucleus, U2-type spliceosome

#### 3.2 蛋白大小评估

439 aa (52.0 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 11 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- U2 spliceosome component with 12 cryo-EM PDB entries. Ultra-novel (PubMed=11). HPA nucleolar localization.

**关键文献**:
1. Dopie J et al. (2020). "Tyramide signal amplification mass spectrometry identifies nuclear speckle proteins." *J Cell Biol*. PMID: 32609799
2. Guvatova ZG et al. (2024). "Matrisome Transcriptome Dynamics during Tissue Aging." *Life (Basel)*. PMID: 38792614
3. Yeh H et al. (1994). "Structure of the human gene encoding the associated microfibrillar protein (MFAP1)." *Genomics*. PMID: 7835894
4. Liu W et al. (1997). "The gene for microfibril-associated protein-1 (MFAP1)." *Hum Genet*. PMID: 9150721
5. Walker L et al. (2024). "Defining Splicing Factor Requirements for Androgen Receptor Variant Synthesis in Advanced Prostate Cancer." *Mol Cancer Res*. PMID: 39348093

**评价**: U2 spliceosome component with 12 cryo-EM PDB entries. Ultra-novel (PubMed=11). HPA nucleolar localization.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 71.31 |
| 有序区域 (pLDDT>70) 占比 | 66.3% |
| 可用 PDB 条目 | 12 个 (5F5S, 5O9Z, 6AHD, 7AAV, 7ABF, 7ABG, 7ABI, 8H6K, 8Q7N, 8QO9, 8QPE, 8QZS) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/MFAP1/MFAP1-PAE.png]]

**评价**: U2-type spliceosome component. Part of pre-catalytic spliceosome. 12 cryo-EM PDB entries. Spliceosome structural component.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | MFAP1 domain (PF06991) |

**染色质调控潜力分析**: U2-type spliceosome component. Part of pre-catalytic spliceosome. 12 cryo-EM PDB entries. Spliceosome structural component.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| ALKBH8, AMOTL2, AP2M1, BEND7, BICD2, BLZF1, CARD9, CDC14B, C | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| STRING 数据不可用 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: centrosome, microfibril, nucleoplasm, nucleus, U2-type precatalytic spliceosome, U2-type spliceosomal complex

**IntAct 查询记录**: IntAct: 15+ 相互作用因子

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: U2 spliceosome component with 12 cryo-EM PDB entries. Ultra-novel (PubMed=11). HPA nucleolar localization.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=71.31, PDB=12条目 | — |
| 结构域 | UniProt / InterPro / Pfam | MFAP1 domain (PF06991) | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus (UniProt), HPA: Nucleoli|Nucleoli fibrillar center,  | — |

**互证加分明细**:
- —
**总分**: +1 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. Ultra-novel (PubMed=11)
2. 12 PDB cryo-EM structures (spliceosome)
3. HPA nucleolar localization (Nucleoli fibrillar center)
4. Well-defined structural role in spliceosome

**风险/不确定性**:
1. Spliceosome rather than chromatin/transcription
2. No DNA/chromatin-binding domains
3. Function depends on spliceosome context

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/P55081
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55081
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MFAP1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/P55081


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MFAP1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/MFAP1/MFAP1-PAE.png]]


