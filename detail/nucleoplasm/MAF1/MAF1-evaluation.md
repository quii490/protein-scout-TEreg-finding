---
type: protein-evaluation
gene: "MAF1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAF1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAF1 /  |
| 蛋白大小 | 256 aa / 28.8 kDa |
| UniProt ID | [Q9H063](https://www.uniprot.org/uniprot/Q9H063) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAF1/IF_images/OE19_1.jpg|OE19]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAF1/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus + Cytoplasm (UniProt), HPA: Nuclear bodies |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 256 aa, 28.8 kDa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed = 84 篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | pLDDT = 76.75, PDB = 1 条目 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | Maf1 domain (PF09174) |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | ARMCX3, CSNK2A1, HTT, PCNA, WFS1 |
| ➕ 互证加分 | — | max +3 | +1 | — |
| **原始总分** |  |  | **100/183** |  |
| **归一化总分** |  |  | **54.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | IF image available (embedded above) | See IF_images/ |
| UniProt | Nucleus + Cytoplasm (UniProt), HPA: Nuclear bodies|Nucleoplasm, GO: nucleoplasm, nucleus | Experimental/ECO evidence |

**结论**: Nucleus + Cytoplasm (UniProt), HPA: Nuclear bodies|Nucleoplasm, GO: nucleoplasm, nucleus

#### 3.2 蛋白大小评估

256 aa (28.8 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 84 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- RNA Polymerase III master repressor regulated by mTOR. Central metabolic sensor. HPA Nuclear bodies+Nucleoplasm. PCNA interaction links to DNA replication.

**关键文献**:
1. Graczyk D et al. (2018). "Regulation of tRNA synthesis by the general transcription factors of RNA polymerase III." *Biochim Biophys Acta Gene Regul Mech*. PMID: 29378333
2. Michels AA et al. (2011). "MAF1: a new target of mTORC1." *Biochem Soc Trans*. PMID: 21428925
3. Chen S et al. (2020). "Maf1 Ameliorates Sepsis-Associated Encephalopathy." *Front Immunol*. PMID: 33424842
4. Wei X et al. (2025). "Feedback loop centered on MAF1 reduces blood-brain barrier damage in sepsis-associated encephalopathy." *Cell Mol Biol Lett*. PMID: 39833662
5. Huang Y et al. (2025). "SERBP1-PCIF1 complex-controlled m6Am modification in glutamatergic neurons." *Nat Commun*. PMID: 40764612

**评价**: RNA Polymerase III master repressor regulated by mTOR. Central metabolic sensor. HPA Nuclear bodies+Nucleoplasm. PCNA interaction links to DNA replication.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 76.75 |
| 有序区域 (pLDDT>70) 占比 | 69.9% |
| 可用 PDB 条目 | 1 个 (3NR5) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAF1/MAF1-PAE.png]]

**评价**: Maf1 is a conserved RNA polymerase III repressor regulated by mTOR signaling. Central metabolic sensor linking nutrient availability to tRNA transcription.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | Maf1 domain (PF09174) |

**染色质调控潜力分析**: Maf1 is a conserved RNA polymerase III repressor regulated by mTOR signaling. Central metabolic sensor linking nutrient availability to tRNA transcription.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| ARMCX3, CSNK2A1, HTT, PCNA, WFS1 | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| STRING 数据不可用 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: nucleoplasm, nucleus, axon, cytoplasm, cytosol, perinuclear region, plasma membrane

**IntAct 查询记录**: IntAct: CSNK2A1 (CK2 kinase) 物理互作, 磷酸化调控 MAF1

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: RNA Polymerase III master repressor regulated by mTOR. Central metabolic sensor. HPA Nuclear bodies+Nucleoplasm. PCNA interaction links to DNA replication.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=76.75, PDB=1条目 | — |
| 结构域 | UniProt / InterPro / Pfam | Maf1 domain (PF09174) | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus + Cytoplasm (UniProt), HPA: Nuclear bodies|Nucleopla | — |

**互证加分明细**:
- —
**总分**: +1 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. Clear functional role: Pol III master repressor
2. HPA Nuclear bodies+Nucleoplasm
3. mTOR signaling link (metabolic sensor)
4. PDB structure (3NR5)
5. PCNA interaction links to DNA replication

**风险/不确定性**:
1. Relatively well-studied (PubMed=84)
2. No chromatin/DNA-binding domains
3. Cytoplasmic shuttling complicates study
4. Pol III rather than chromatin/Pol II regulation

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q9H063
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H063
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAF1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q9H063


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MAF1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAF1/MAF1-PAE.png]]




