---
type: protein-evaluation
gene: "MDFIC"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MDFIC 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MDFIC |
| 别名 | HIC, MDFIC1 |
| 基因全称 | MyoD family inhibitor domain containing |
| 蛋白名称 | MyoD family inhibitor domain-containing protein |
| 蛋白大小 | 246 aa |
| UniProt ID | Q9P1T7 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 4/10 | x4 | 16 | HPA: Nuclear bodies, Nuclear membrane, Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 246 aa |
| Novelty 研究新颖性 | 8/10 | x5 | 40 | PubMed: 22 篇 |
| 3D Structure 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT=52.9 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 无已注释染色质调控结构域 |
| PPI Network PPI网络 | 8/10 | x3 | 24 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
| **原始总分** |  |  | **123/183** |  |
| **归一化总分** |  |  | **67.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt |  | — |
| GO-CC | GO:0005634 Nucleus (ND) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MDFIC/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MDFIC/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

246 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 22 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Zhou Z et al. (2023). "Mechanisms of PIEZO Channel Inactivation.". *Int J Mol Sci*. PMID: 37762415
2. Zhou Z et al. (2023). "MyoD-family inhibitor proteins act as auxiliary subunits of Piezo channels.". *Science*. PMID: 37590348
3. Shan Y et al. (2025). "Structure of human PIEZO1 and its slow-inactivating channelopathy mutants.". *Elife*. PMID: 40668110
4. Habib AM et al. (2025). "MDFIC2 is a PIEZO channel modulator that can alleviate mechanical allodynia associated with neuropathic pain.". *Proc Natl Acad Sci U S A*. PMID: 41201821
5. Chen CJ et al. (2020). "The MyoD family inhibitor domain-containing protein enhances the chemoresistance of cancer stem cells in the epithelial state by increasing β-catenin activity.". *Oncogene*. PMID: 31911618


**评价**: PubMed 22 篇，属非常新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 52.9 |
| pLDDT > 90 占比 | 0.0% |
| pLDDT 70-90 占比 | 8.5% |
| pLDDT 50-70 占比 | 49.6% |
| pLDDT < 50 占比 | 41.9% |
| 可用 PDB 条目 | 4 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MDFIC/MDFIC-PAE.png]]

**评价**: AlphaFold 预测较低质量，大部分区域无序 (AlphaFold v6, pLDDT=52.9, >90=0%, 70-90=8%, 50-70=50%, <50=42%. PDB entries: 8YFC, 8YFG, 8ZU3, 9VMX)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 无已注释染色质调控结构域

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-488313|ensembl:ENSMUSP00000064448.6|ensembl:ENSMUSP00000109992.2 | MI:0018(two hybrid) | PMID:pubmed:15102471 | — | — |
| intact:EBI-3942425|ensembl:ENSP00000341327.2|ensembl:ENSP00000378855.2|ensembl:ENSP00000452522.1 | MI:0018(two hybrid) | PMID:imex:IM-15364|pubmed:21988832 | — | — |
| intact:EBI-2812899|uniprotkb:Q9P1T6|ensembl:ENSP00000377126.1 | MI:0398(two hybrid pooling approach | PMID:imex:IM-13779|pubmed:20711500 | — | — |
| intact:EBI-2812917|uniprotkb:Q6I2B1|uniprotkb:Q6F0C3|uniprotkb:E9R6N6|uniprotkb:E9R6N7|uniprotkb:A0A2P0HB35|uniprotkb:Q81U26 | MI:0398(two hybrid pooling approach | PMID:imex:IM-13779|pubmed:20711500 | — | — |
| intact:EBI-2812854|uniprotkb:Q6KMM3|uniprotkb:Q6HTD1|uniprotkb:E9QZR3|uniprotkb:E9QZR4|uniprotkb:A0A2P0HJA3|uniprotkb:Q81LX9 | MI:0398(two hybrid pooling approach | PMID:imex:IM-13779|pubmed:20711500 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CTCF | 0.0 | — | — |
| CHIA | 0.0 | — | — |
| CCNT1 | 0.0 | — | — |
| RAD21 | 0.0 | — | — |
| FBL | 0.0 | — | — |
| THBS1 | 0.0 | — | — |
| TMEM168 | 0.0 | — | — |
| ZIC2 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 9
- 仅 IntAct 实验: 10
- 调控相关比例: 2/9 (22%)

**评价**: PPI 得分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=52.9, PDB=4 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 9/10/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nuclear bodies, Nuclear membrane, Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
- PDB 多条目 (>=3) (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 非常新颖 (PubMed 22 篇)，几乎未被研究
2. HPA 确认核定位，中等置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=52.9)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MDFIC
- Protein Atlas: https://www.proteinatlas.org/MDFIC
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MDFIC
- UniProt: https://www.uniprot.org/uniprotkb/Q9P1T7
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P1T7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MDFIC-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MDFIC/MDFIC-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P1T7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 74..246; /note="MDFI" |
| InterPro | IPR026134; |
| Pfam | PF15316; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135272-MDFIC/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCNT1 | Biogrid | false |
| CDK9 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
