---
type: protein-evaluation
gene: "MAB21L1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAB21L1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAB21L1 / CAGR1 |
| 蛋白大小 | 359 aa / 41.0 kDa |
| UniProt ID | [Q13394](https://www.uniprot.org/uniprot/Q13394) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAB21L1/IF_images/BJ-Human-fibroblast_1.jpg|BJ [Human fibroblast]]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAB21L1/IF_images/Rh30_1.jpg|Rh30]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | Nucleus (UniProt), GO: nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 359 aa, 41.0 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed = 30 篇 |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | pLDDT = 93.88, PDB = 2 条目 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | Mab-21-like nucleotidyltransferase (PF03281), Mab-21 HhH/H2TH-like (PF20266) |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | PBX2, SIAH1 |
| ➕ 互证加分 | — | max +3 | +0 | — |
| **原始总分** |  |  | **128/183** |  |
| **归一化总分** |  |  | **69.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | IF image available (embedded above) | See IF_images/ |
| UniProt | Nucleus (UniProt), GO: nucleus | Experimental/ECO evidence |

**结论**: Nucleus (UniProt), GO: nucleus

#### 3.2 蛋白大小评估

359 aa (41.0 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 30 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- Nucleotidyltransferase fold nuclear protein with strong structural quality (pLDDT 93.9). Potentially a DNA/RNA modifying enzyme. Limited functional characterization.

**关键文献**:
1. de Oliveira Mann CC et al. (2016). "Structural and biochemical characterization of the cell fate determining nucleotidyltransferase fold protein MAB21L1." *Sci Rep*. PMID: 27271801
2. Yamada R et al. (2021). "MAB21L1 modulates gene expression and DNA metabolic processes in the lens placode." *Dis Model Mech*. PMID: 34779479
3. Hall HN et al. (2022). "Monoallelic variants resulting in substitutions of MAB21L1 Arg51 Cause Aniridia and microphthalmia." *PLoS One*. PMID: 36413568
4. Li J et al. (2024). "Monoallelic missense variants in MAB21L1 cause a novel autosomal dominant microphthalmia." *Ophthalmic Genet*. PMID: 39016008
5. Vollger MR et al. (2025). "Synchronized long-read genome, methylome, epigenome and transcriptome profiling resolve a Mendelian condition." *Nat Genet*. PMID: 39880924

**评价**: Nucleotidyltransferase fold nuclear protein with strong structural quality (pLDDT 93.9). Potentially a DNA/RNA modifying enzyme. Limited functional characterization.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 93.88 |
| 有序区域 (pLDDT>70) 占比 | 97.2% |
| 可用 PDB 条目 | 2 个 (5EOG, 5EOM) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAB21L1/MAB21L1-PAE.png]]

**评价**: Nucleotidyltransferase fold with HhH motif suggestive of nucleic acid binding. Distantly related to DNA/RNA modifying enzymes. Strong structural quality.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | Mab-21-like nucleotidyltransferase (PF03281), Mab-21 HhH/H2TH-like (PF20266) |

**染色质调控潜力分析**: Nucleotidyltransferase fold with HhH motif suggestive of nucleic acid binding. Distantly related to DNA/RNA modifying enzymes. Strong structural quality.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| PBX2, SIAH1 | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| STRING 数据不可用 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: nucleus

**IntAct 查询记录**: IntAct 查询无物理互作记录

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: Nucleotidyltransferase fold nuclear protein with strong structural quality (pLDDT 93.9). Potentially a DNA/RNA modifying enzyme. Limited functional characterization.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=93.88, PDB=2条目 | — |
| 结构域 | UniProt / InterPro / Pfam | Mab-21-like nucleotidyltransferase (PF03281), Mab-21 HhH/H2T | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus (UniProt), GO: nucleus | — |

**互证加分明细**:
- —
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. Excellent structural quality (pLDDT 93.88, 97.2% ordered)
2. Clear nuclear localization (UniProt Nucleus + GO:nucleus)
3. Nucleotidyltransferase fold with HhH motif suggests enzymatic function
4. PDB experimental structures (5EOG, 5EOM)

**风险/不确定性**:
1. Extremely limited functional characterization
2. No known chromatin/DNA-binding domains
3. Minimal PPI data
4. PubMed mostly developmental biology/ophthalmology

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q13394
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13394
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAB21L1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q13394


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MAB21L1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAB21L1/MAB21L1-PAE.png]]




