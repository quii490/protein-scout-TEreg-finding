---
type: protein-evaluation
gene: "FOXN3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FOXN3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXN3 |
| 蛋白大小 | 490 aa |
| UniProt ID | O00409 (Forkhead box protein N3) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXN3/IF_images/PODO-TERT256_1.jpg|PODO/TERT256]]


### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | x4 | 32 | HPA 标注: Nucleoplasm |
| 📏 蛋白大小 | 10/10 | x1 | 10 | 490 aa |
| 🆕 研究新颖性 | 2/10 | x5 | 30 | PubMed 86 篇 |
| 🏗️ 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT 57.6, v6 |
| 🧬 调控结构域 | 10/10 | x2 | 20 | InterPro 7 个结构域条目 |
| 🔗 PPI 网络 | 6/10 | x3 | 18 | STRING 24 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
|  | **原始总分** |  | **108.5/183** | **108.0/183** |  |  |  |
|  | **归一化总分** |  | **59.3/100** | **59.0/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | Nucleoplasm | Tier1 |
| UniProt |  | — |

**结论**: HPA 标注: Nucleoplasm。核定位得分 8/10。

**IF 图片**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 490 aa
- 大小适宜性评分：10/10

**评价**: 490 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 86 |
| 新颖性评分 | 6/10 |

**评价**: PubMed 86 篇，属于有一定研究但 niche 空间充足。

**关键文献**:
1. Yu J et al. (2025). "Phosphorylation of FOXN3 by NEK6 promotes pulmonary fibrosis through Smad signaling". *Nat Commun*. PMID: 39984467
2. Zhu X et al. (2023). "p38-mediated FOXN3 phosphorylation modulates lung inflammation and injury through the NF-κB signaling pathway". *Nucleic Acids Res*. PMID: 36794705
3. Liu X et al. (2024). "Single-Nucleus Multiomic Analyses Identifies Gene Regulatory Dynamics of Phenotypic Modulation in Human Aneurysmal Aortic Root". *Adv Sci (Weinh)*. PMID: 38552156
4. Zhu X et al. (2026). "PARP1 stabilizes FOXN3 to suppress pulmonary fibrosis through p38-related feedback regulation". *Sci Adv*. PMID: 41481720
5. Karanth S et al. (2016). "FOXN3 Regulates Hepatic Glucose Utilization". *Cell Rep*. PMID: 27292639
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 57.6 |
| 有序区域 (pLDDT>70) 占比 | 24.3% |
| pLDDT>90 占比 | 15.7% |
| pLDDT 70-90 占比 | 8.6% |
| pLDDT 50-70 占比 | 21.2% |
| pLDDT<50 占比 | 54.5% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXN3/FOXN3-PAE.png]]

**评价**: AlphaFold预测质量偏低（pLDDT=57.6）。大量无序区域。评分 6/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| Fork head domain | IPR |
| Fork head domain conserved site1 | IPR |
| Fork head domain conserved site 2 | IPR |
| Winged helix-like DNA-binding domain superfamily | IPR |
| Winged helix DNA-binding domain superfamily | IPR |
| Forkhead box protein N2/3-like | IPR |
| Forkhead box protein N3, forkhead domain | IPR |

**染色质调控潜力分析**: InterPro 注释了 7 个结构域条目。包含 forkhead/winged-helix DNA 结合域，为典型转录因子。评分 10/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| SIN3A | 0.956 | — | — |
| MEN1 | 0.866 | — | — |
| SNW1 | 0.863 | — | — |
| ATR | 0.676 | — | — |
| RFX3 | 0.641 | — | — |
| PABPN1 | 0.598 | — | — |
| CYP24A1 | 0.597 | — | — |
| HDAC3 | 0.591 | — | — |
| HDAC1 | 0.567 | — | — |
| HDAC2 | 0.564 | — | — |

**GO-CC 复合体**: 从 UniProt GO 注释提取

**PPI 互证分析**:
- STRING 高置信度 (>0.7) partners: 3 个
- 调控相关比例: 待进一步分析

**评价**: STRING 数据库显示 24 个互作伙伴。评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT 57.6 | — |
| 结构域 | InterPro | 7 个条目 | — |
| PPI | STRING | 24 partners | — |
| 定位 | HPA / UniProt | Nucleoplasm | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (4.0/5)

**核心优势**:
1. 较新颖，PubMed ≤100 篇
2. 核蛋白候选

**风险/不确定性**:
1. AlphaFold 预测质量偏低，大量无序区域
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FOXN3 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FOXN3 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00409
- Protein Atlas: https://www.proteinatlas.org/search/FOXN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00409
- STRING: https://string-db.org/network/9606.FOXN3
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/O00409/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FOXN3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXN3/FOXN3-PAE.png]]


