---
type: protein-evaluation
gene: "FOXR1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FOXR1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXR1 |
| 蛋白大小 | 292 aa |
| UniProt ID | Q6PIV2 (Forkhead box protein R1) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FOXR1/IF_images/HaCaT_1.jpg|HaCaT]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FOXR1/IF_images/RT-4_1.jpg|RT-4]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | x4 | 32 | HPA 标注: Nucleoli , Nucleoplasm |
| 📏 蛋白大小 | 10/10 | x1 | 10 | 292 aa |
| 🆕 研究新颖性 | 10/10 | x5 | 50 | PubMed 17 篇 |
| 🏗️ 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT 66.3, v6 |
| 🧬 调控结构域 | 10/10 | x2 | 20 | InterPro 4 个结构域条目 |
| 🔗 PPI 网络 | 4/10 | x3 | 12 | STRING 0 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
| **原始总分** |  |  | **145.5/183** |  |
| **归一化总分** |  |  | **79.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | Nucleoli|Nucleoplasm | Tier1 |
| UniProt | , ,  | — |

**结论**: HPA 标注: Nucleoli|Nucleoplasm。核定位得分 8/10。

**IF 图片**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 292 aa
- 大小适宜性评分：10/10

**评价**: 292 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 17 |
| 新颖性评分 | 10/10 |

**关键文献**:
1. Katoh et al. (2004). "Human FOX gene family (Review).". *Int J Oncol*. PMID: 15492844
2. Linos et al. (2024). "Untying the Gordian knot of composite hemangioendothelioma: Discovery of novel fusions.". *Genes Chromosomes Cancer*. PMID: 37658696
3. Mota et al. (2021). "FOXR1 regulates stress response pathways and is necessary for proper brain development.". *PLoS Genet*. PMID: 34723967
4. Katoh et al. (2013). "Cancer genetics and genomics of human FOX family genes.". *Cancer Lett*. PMID: 23022474
5. Waxman et al. (2025). "Foxr1 deletion causes microcephaly and leads to cortical and hippocampal hypoplasia.". *Front Neurosci*. PMID: 40497137
**评价**: PubMed 17 篇，属于极度新颖，几乎未被研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 66.3 |
| 有序区域 (pLDDT>70) 占比 | 39.7% |
| pLDDT>90 占比 | 26.0% |
| pLDDT 70-90 占比 | 13.7% |
| pLDDT 50-70 占比 | 28.4% |
| pLDDT<50 占比 | 31.8% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FOXR1/FOXR1-PAE.png]]

**评价**: AlphaFold中等质量预测（pLDDT=66.3）。部分区域有序。评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| Fork head domain | IPR |
| Winged helix-like DNA-binding domain superfamily | IPR |
| Winged helix DNA-binding domain superfamily | IPR |
| Forkhead box transcription regulators | IPR |

**染色质调控潜力分析**: InterPro 注释了 4 个结构域条目。包含 forkhead/winged-helix DNA 结合域，为典型转录因子。评分 10/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| PPCDC | two hybrid array | 31515488 | — | — |
| GMCL1 | two hybrid array | 32296183 | — | — |
| CEP19 | validated two hybrid | 32296183 | — | — |
| DPPA4 | validated two hybrid | 32296183 | — | — |
| BANP | two hybrid array | 32296183 | — | — |
| FLJ13057 | two hybrid array | 25416956 | — | — |
| MEOX2 | two hybrid array | 25416956 | — | — |
| HTT | two hybrid array | 32814053 | — | — |
| GDAP1 | two hybrid array | 32814053 | — | — |
| PEX26 | two hybrid array | 32814053 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度互作伙伴 | — | — | — |

**GO-CC 复合体**: 从 UniProt GO 注释提取

**PPI 互证分析**:
- STRING 高置信度 (>0.7) partners: 0 个
- 调控相关比例: 待进一步分析

**评价**: STRING 数据库显示 0 个互作伙伴。评分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT 66.3 | — |
| 结构域 | InterPro | 4 个条目 | — |
| PPI | STRING | 0 partners | — |
| 定位 | HPA / UniProt | Nucleoli|Nucleoplasm | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (4.0/5)

**核心优势**:
1. 极度新颖，PubMed ≤20 篇
2. AlphaFold 结构中等

**风险/不确定性**:
1. 结构质量中等
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FOXR1 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FOXR1 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PIV2
- Protein Atlas: https://www.proteinatlas.org/search/FOXR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PIV2
- STRING: https://string-db.org/network/9606.FOXR1
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q6PIV2/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FOXR1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/FOXR1/FOXR1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PIV2 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001766;IPR052328;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176302-FOXR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| A2M | Intact | false |
| BANP | Intact | false |
| BRD8 | Biogrid | false |
| CEP19 | Intact | false |
| DMAP1 | Biogrid | false |
| DPPA4 | Intact | false |
| EP400 | Biogrid | false |
| EPC1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
