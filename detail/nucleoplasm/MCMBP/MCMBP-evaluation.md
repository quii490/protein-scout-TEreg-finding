---
type: protein-evaluation
gene: "MCMBP"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MCMBP 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MCMBP / C10orf119 |
| 蛋白大小 | 642 aa / 73.0 kDa |
| UniProt ID | [Q9BTE3](https://www.uniprot.org/uniprot/Q9BTE3) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus (UniProt), HPA: Nucleoplasm, GO: nucleoplasm, nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 642 aa, 73.0 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed = 14 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | pLDDT = None, PDB = 1 条目 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | MCM complex-binding domain (PF09739) |
| 🔗 PPI 网络 | 8/10 | ×3 | 24 | CDC7, GINS2, GINS4, MCM2, MCM3, MCM4, MCM5, MCM6, MCM7, MCM8 |
| ➕ 互证加分 | — | max +3 | +2 | — |
| **原始总分** |  |  | **152/183** |  |
| **归一化总分** |  |  | **83.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis），核定位基于 HPA 标注（Nucleoplasm）+ UniProt + GO | — |
| UniProt | Nucleus (UniProt), HPA: Nucleoplasm, GO: nucleoplasm, nucleus | Experimental/ECO evidence |

**结论**: Nucleus (UniProt), HPA: Nucleoplasm, GO: nucleoplasm, nucleus

#### 3.2 蛋白大小评估

642 aa (73.0 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 14 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- MCM complex binding protein with extensive physical interactions with the replicative helicase. Direct DNA replication role. Ultra-novel (PubMed=14).

**关键文献**:
1. Yadav AK et al. (2025). "CRL4(DCAF12) regulation of MCMBP ensures optimal licensing of DNA replication." *Nat Commun*. PMID: 41145411
2. Wang J et al. (2025). "DNA replication fork speed acts as a pacer in cortical neurogenesis." *Nat Commun*. PMID: 41253827
3. Hatoyama Y et al. (2023). "The assembly of the MCM2-7 hetero-hexamer and its significance in DNA replication." *Biochem Soc Trans*. PMID: 37145026
4. Zhang X et al. (2025). "Multiomics profiling identifies MCMBP as a prognostic biomarker in pancreatic ductal adenocarcinoma." *Front Immunol*. PMID: 41346611
5. Quimbaya M et al. (2014). "Deregulation of the replisome factor MCMBP prompts oncogenesis in colorectal carcinomas." *Neoplasia*. PMID: 25246271

**评价**: MCM complex binding protein with extensive physical interactions with the replicative helicase. Direct DNA replication role. Ultra-novel (PubMed=14).

#### 3.4 三维结构分析

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | None |
| 有序区域 (pLDDT>70) 占比 | None% |
| 可用 PDB 条目 | 1 个 (4KG9) |

**PAE 图**:
PAE 图片未获取

**评价**: MCM complex-binding protein. Binds MCM2-7 replicative helicase. Directly regulates DNA replication licensing. PDB structure available.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | MCM complex-binding domain (PF09739) |

**染色质调控潜力分析**: MCM complex-binding protein. Binds MCM2-7 replicative helicase. Directly regulates DNA replication licensing. PDB structure available.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| CDC7, GINS2, GINS4, MCM2, MCM3, MCM4, MCM5, MCM6, MCM7, MCM8 | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| STRING 数据不可用 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: nucleoplasm, nucleus, cytosol, cell junction

**IntAct 查询记录**: IntAct: 大量 MCM 复合体成员物理互作 (MCM2-7, CDC7, GINS2, GINS4)

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: MCM complex binding protein with extensive physical interactions with the replicative helicase. Direct DNA replication role. Ultra-novel (PubMed=14).

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=None, PDB=1条目 | — |
| 结构域 | UniProt / InterPro / Pfam | MCM complex-binding domain (PF09739) | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus (UniProt), HPA: Nucleoplasm, GO: nucleoplasm, nucleu | — |

**互证加分明细**:
- —
**总分**: +2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. Ultra-novel (PubMed=14)
2. Extensive physical PPI with MCM complex (co-IP evidence)
3. Direct DNA replication role
4. PDB structure (4KG9)
5. HPA Nucleoplasm + UniProt Nucleus

**风险/不确定性**:
1. AlphaFold PAE download failed
2. Only one PDB entry
3. DNA replication rather than transcription/chromatin
4. No chromatin/DNA-binding structural domain

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q9BTE3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BTE3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MCMBP%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q9BTE3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。
