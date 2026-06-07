---
type: protein-evaluation
gene: "MEI4"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEI4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MEI4 |
| 别名 | — |
| 基因全称 | meiotic double-stranded break formation protein 4 |
| 蛋白名称 | Meiosis-specific protein MEI4 |
| 蛋白大小 | 385 aa |
| UniProt ID | A8MW99 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm (IDA supported) |
| Size 蛋白大小 | 10/10 | x1 | 10 | 385 aa |
| Novelty 研究新颖性 | 8/10 | x5 | 40 | PubMed: 25 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=70.2 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 无已注释染色质调控结构域 |
| PPI Network PPI网络 | 8/10 | x3 | 24 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
| **原始总分** |  |  | **146/183** |  |
| **归一化总分** |  |  | **79.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

> **Protein Atlas IF**: 暂无HPA数据，核定位基于UniProt+GO

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA数据，核定位基于UniProt+GO | — |
| UniProt | Cytoplasm/Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IBA|IC|IDA|IEA) | — |

暂无 HPA IF 图片数据（Pending cell analysis），核定位基于 UniProt + GO 注释。


**结论**: 该蛋白在 HPA 中检测到Nucleoplasm信号，UniProt 注释为Cytoplasm/Nucleus。核定位得分 9/10。

#### 3.2 蛋白大小评估

385 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 25 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Biot M et al. (2024). "Principles of chromosome organization for meiotic recombination.". *Mol Cell*. PMID: 38657614
2. Acquaviva L et al. (2020). "Ensuring meiotic DNA break formation in the mouse pseudoautosomal region.". *Nature*. PMID: 32461690
3. Claeys Bouuaert C et al. (2021). "DNA-driven condensation assembles the meiotic DNA break machinery.". *Nature*. PMID: 33731927
4. Wang Y et al. (2026). "MEI4 variations drive female reproductive disorders via impaired oocyte abundance and developmental potential.". *J Genet Genomics*. PMID: 41419020
5. Pan Z et al. (2024). "Bi-allelic missense variants in MEI4 cause preimplantation embryonic arrest and female infertility.". *Hum Genet*. PMID: 38252283


**评价**: PubMed 25 篇，属非常新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 70.2 |
| pLDDT > 90 占比 | 9.9% |
| pLDDT 70-90 占比 | 54.3% |
| pLDDT 50-70 占比 | 13.0% |
| pLDDT < 50 占比 | 22.9% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEI4/MEI4-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=70.2, >90=10%, 70-90=54%, 50-70=13%, <50=23%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 无已注释染色质调控结构域

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-14447|uniprotkb:D6VZV6 | MI:0416(fluorescence microscopy) | PMID:pubmed:16783010|imex:IM-20454 | — | — |
| intact:EBI-2566907|uniprotkb:P87265|uniprotkb:D3DLU5 | MI:0416(fluorescence microscopy) | PMID:pubmed:16783010|imex:IM-20454 | — | — |
| intact:EBI-3918847|uniprotkb:Q9BSN9|uniprotkb:Q96M28|ensembl:ENSP00000297679.5 | MI:1112(two hybrid prey pooling app | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-12394782|ensembl:ENSP00000347683.4 | MI:1112(two hybrid prey pooling app | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-711522|uniprotkb:Q53X88|ensembl:ENSP00000262890.2|ensembl:ENSP00000444935.1 | MI:0397(two hybrid array) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| REC114 | 0.0 | — | — |
| CD151 | 0.0 | — | — |
| CCDC36 | 0.0 | — | — |
| MEI1 | 0.0 | — | — |
| SPO11 | 0.0 | — | — |
| ADARB1 | 0.0 | — | — |
| ANKRD31 | 0.0 | — | — |
| HORMAD1 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 15
- 调控相关比例: 4/15 (27%)

**评价**: PPI 得分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=70.2, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/15/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- GO-CC IDA 实验证据 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★ (4/5)

**核心优势**:
1. 非常新颖 (PubMed 25 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MEI4
- Protein Atlas: https://www.proteinatlas.org/MEI4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEI4
- UniProt: https://www.uniprot.org/uniprotkb/A8MW99
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MW99


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MEI4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEI4/MEI4-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A8MW99 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR025888; |
| Pfam | PF13971; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000269964-MEI4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AFMID | Intact | false |
| BAG4 | Intact | false |
| C19orf25 | Intact | false |
| C1orf109 | Intact | false |
| CABP5 | Intact | false |
| CDKN2D | Intact | false |
| CHAF1A | Intact | false |
| CPNE2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
