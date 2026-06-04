---
type: protein-evaluation
gene: "MRTFB"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MRTFB 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MRTFB / KIAA1243, MKL2 |
| 蛋白大小 | 1088 aa / 118.1 kDa |
| UniProt ID | [Q9ULH7](https://www.uniprot.org/uniprot/Q9ULH7) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus (UniProt), GO: nucleus, cytoplasm, glutamate synapse |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1088 aa, 118.1 kDa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed = 65 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | pLDDT = 52.25, PDB = 0 条目 |
| 🧬 调控结构域 | 10/10 | ×2 | 20 | SAP domain (PF02037), RPEL repeat (Myocardin-like) |
| 🔗 PPI 网络 | 8/10 | ×3 | 24 | SRF |
| ➕ 互证加分 | — | max +3 | +2 | — |
| **原始总分** |  |  | **124/183** |  |
| **归一化总分** |  |  | **67.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis），核定位基于 UniProt + GO（nucleus） | — |
| UniProt | Nucleus (UniProt), GO: nucleus, cytoplasm, glutamate synapse | Experimental/ECO evidence |

**结论**: Nucleus (UniProt), GO: nucleus, cytoplasm, glutamate synapse

#### 3.2 蛋白大小评估

1088 aa (118.1 kDa)，在理想生化实验范围（200-800 aa）外。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 65 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- Myocardin-related transcription factor with SAP DNA-binding domain. Direct SRF coactivator. Rho-actin-MRTF-SRF signaling axis. Nuclear-cytoplasmic shuttling.

**关键文献**:
1. Kodama T et al. (2019). "MRTFB suppresses colorectal cancer development through regulating SPDL1 and MCAM." *Proc Natl Acad Sci U S A*. PMID: 31690663
2. Ihara D et al. (2025). "Neuronal Plasticity-related Mechanisms Triggered by the Transcriptional Coactivator MRTFB." *Yakugaku Zasshi*. PMID: 41320266
3. Wilk SM et al. (2025). "Multiplex imaging reveals novel patterns of MRTFA/B activation in the breast cancer microenvironment." *J Transl Med*. PMID: 40448123
4. Garg B et al. (2025). "MICAL2 Promotes Pancreatic Cancer Growth and Metastasis." *Cancer Res*. PMID: 39745352
5. Yang C et al. (2025). "HIV-1 latency: From acquaintance to confidant." *J Virus Erad*. PMID: 40497153

**评价**: Myocardin-related transcription factor with SAP DNA-binding domain. Direct SRF coactivator. Rho-actin-MRTF-SRF signaling axis. Nuclear-cytoplasmic shuttling.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 52.25 |
| 有序区域 (pLDDT>70) 占比 | 23.1% |
| 可用 PDB 条目 | 0 个 (—) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MRTFB/MRTFB-PAE.png]]

**评价**: SAP domain: DNA-binding domain in chromatin-associated proteins. Myocardin family transcriptional coactivator. Partners with SRF to regulate cytoskeletal genes.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | SAP domain (PF02037), RPEL repeat (Myocardin-like) |

**染色质调控潜力分析**: SAP domain: DNA-binding domain in chromatin-associated proteins. Myocardin family transcriptional coactivator. Partners with SRF to regulate cytoskeletal genes.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| SRF | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| SRF(0.978), PHACTR1(0.944), ACTA1(0.914), RHOA(0.806), RBM15(0.749), BACH2(0.540 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: cytoplasm, glutamatergic synapse, nucleus, postsynapse, presynapse

**IntAct 查询记录**: IntAct: SRF 直接物理互作 (MRTFB-SRF 转录复合体)

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: Myocardin-related transcription factor with SAP DNA-binding domain. Direct SRF coactivator. Rho-actin-MRTF-SRF signaling axis. Nuclear-cytoplasmic shuttling.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=52.25, PDB=0条目 | — |
| 结构域 | UniProt / InterPro / Pfam | SAP domain (PF02037), RPEL repeat (Myocardin-like) | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus (UniProt), GO: nucleus, cytoplasm, glutamate synapse | — |

**互证加分明细**:
- —
**总分**: +2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. SAP domain = bonafide chromatin/DNA-binding
2. Direct SRF interaction (TF partnership)
3. Myocardin family - defined transcriptional role
4. Rho-actin-MRTF-SRF signaling axis

**风险/不确定性**:
1. Large protein (1088aa, size score 8)
2. Poor AlphaFold quality (pLDDT 52.3)
3. No PDB structures
4. Moderate novelty (PubMed=65)
5. Nuclear-cytoplasmic shuttling

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q9ULH7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULH7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MRTFB%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q9ULH7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MRTFB-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MRTFB/MRTFB-PAE.png]]
