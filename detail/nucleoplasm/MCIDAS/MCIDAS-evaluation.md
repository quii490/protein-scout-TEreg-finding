---
type: protein-evaluation
gene: "MCIDAS"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MCIDAS 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MCIDAS / IDAS, MCI, MCIN |
| 蛋白大小 | 385 aa / 41.7 kDa |
| UniProt ID | [D6RGH6](https://www.uniprot.org/uniprot/D6RGH6) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus (UniProt), GO: nuclear body, nucleoplasm, nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 385 aa, 41.7 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed = 28 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | pLDDT = 60.62, PDB = 1 条目 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | Geminin/Multicilin domain (PF07412) |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | BYSL, GMNN, MCIDAS, TCEANC, ZBTB24 |
| ➕ 互证加分 | — | max +3 | +1 | — |
| **原始总分** |  |  | **133/183** |  |
| **归一化总分** |  |  | **72.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis），核定位基于 UniProt + GO（nuclear body, nucleoplasm, nucleu | — |
| UniProt | Nucleus (UniProt), GO: nuclear body, nucleoplasm, nucleus | Experimental/ECO evidence |

**结论**: Nucleus (UniProt), GO: nuclear body, nucleoplasm, nucleus

#### 3.2 蛋白大小评估

385 aa (41.7 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 28 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- Multicilin - master regulator of multiciliate cell differentiation. Forms transcriptional complex with E2F4/5 and GMNN. One PDB entry.

**关键文献**:
1. Boon M et al. (2014). "MCIDAS mutations result in a mucociliary clearance disorder with reduced generation of multiple motile cilia." *Nat Commun*. PMID: 25048963
2. Bankole A et al. (2025). "mTOR controls ependymal cell differentiation." *EMBO Rep*. PMID: 40307619
3. Manojlovic Z et al. (2017). "La-related protein 6 controls ciliated cell differentiation." *Cilia*. PMID: 28344782
4. Basso M et al. (2025). "Actin-based deformations of the nucleus control mouse multiciliated ependymal cell differentiation." *Dev Cell*. PMID: 39662468
5. Adam MP et al. (1993). "Primary Ciliary Dyskinesia." *GeneReviews*. PMID: 20301301

**评价**: Multicilin - master regulator of multiciliate cell differentiation. Forms transcriptional complex with E2F4/5 and GMNN. One PDB entry.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 60.62 |
| 有序区域 (pLDDT>70) 占比 | 33.2% |
| 可用 PDB 条目 | 1 个 (4BRY) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MCIDAS/MCIDAS-PAE.png]]

**评价**: Master regulator of multiciliate cell differentiation. Forms E2F4/5 transcriptional complex for centriole amplification. Coiled-coil protein.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | Geminin/Multicilin domain (PF07412) |

**染色质调控潜力分析**: Master regulator of multiciliate cell differentiation. Forms E2F4/5 transcriptional complex for centriole amplification. Coiled-coil protein.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| BYSL, GMNN, MCIDAS, TCEANC, ZBTB24 | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| STRING 数据不可用 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: nuclear body, nucleoplasm, nucleus

**IntAct 查询记录**: IntAct: GMNN (geminin) 直接物理互作，形成 E2F 转录调控复合体

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: Multicilin - master regulator of multiciliate cell differentiation. Forms transcriptional complex with E2F4/5 and GMNN. One PDB entry.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=60.62, PDB=1条目 | — |
| 结构域 | UniProt / InterPro / Pfam | Geminin/Multicilin domain (PF07412) | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus (UniProt), GO: nuclear body, nucleoplasm, nucleus | — |

**互证加分明细**:
- —
**总分**: +1 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. Clear transcriptional regulation role (E2F4/5 + Geminin complex)
2. Master regulator of multiciliogenesis
3. PDB structure (4BRY)
4. Reasonable novelty (PubMed=28)

**风险/不确定性**:
1. AlphaFold moderate (pLDDT 60.6, 33.2% ordered)
2. Function specific to ciliated cells
3. Limited disease relevance beyond ciliopathies
4. No DNA-binding domain (coactivator)

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/D6RGH6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/D6RGH6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MCIDAS%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/D6RGH6


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MCIDAS-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MCIDAS/MCIDAS-PAE.png]]
