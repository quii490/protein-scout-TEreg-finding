---
type: protein-evaluation
gene: "MXD3"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MXD3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MXD3 |
| 别名 | MAD3, bHLHc13 |
| 基因全称 | MAX dimerization protein 3 |
| 蛋白名称 | Max dimerization protein 3 |
| 蛋白大小 | 206 aa |
| UniProt ID | Q9BW11 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 4/10 | x4 | 16 | HPA: Nuclear membrane, Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 206 aa |
| Novelty 研究新颖性 | 6/10 | x5 | 30 | PubMed: 54 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=73.4 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含 bHLHZip 结构域，MYC/MAX/MXD 网络成员 |
| PPI Network PPI网络 | 4/10 | x3 | 12 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +0.5 | — |
| **原始总分** |  |  | **103.5/183** |  |
| **归一化总分** |  |  | **56.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | PC-3, MCF-7 | HPA validated |
| UniProt |  | — |
| GO-CC | GO:0005634 Nucleus (IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MXD3/IF_images/MCF_7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MXD3/IF_images/PC_3_1.jpg|PC-3]]
#### 3.2 蛋白大小评估

206 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 54 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Li D et al. (2025). "Prognostic Implications and Therapeutic Potential of MXD Genes in Gastric Cancer.". *Curr Med Chem*. PMID: 40353420
2. Shan G et al. (2025). "Sarcosine sensitizes lung adenocarcinoma to chemotherapy by dual activation of ferroptosis via PDK4/PDHA1 signaling and NMDAR-mediated iron export.". *Exp Hematol Oncol*. PMID: 40275333
3. Shimada Y et al. (2014). "Downregulation of Max dimerization protein 3 is involved in decreased visceral adipose tissue by inhibiting adipocyte differentiation in zebrafish and mice.". *Int J Obes (Lond)*. PMID: 24254064
4. Ngo T et al. (2019). "Alternative Splicing of MXD3 and Its Regulation of MXD3 Levels in Glioblastoma.". *Front Mol Biosci*. PMID: 30838212
5. Zhang X et al. (2021). "MXD3 as an Immunological and Prognostic Factor From Pancancer Analysis.". *Front Mol Biosci*. PMID: 34859046


**评价**: PubMed 54 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 73.4 |
| pLDDT > 90 占比 | 37.9% |
| pLDDT 70-90 占比 | 16.5% |
| pLDDT 50-70 占比 | 26.7% |
| pLDDT < 50 占比 | 18.9% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MXD3/MXD3-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=73.4, >90=38%, 70-90=16%, 50-70=27%, <50=19%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含 bHLHZip 结构域，MYC/MAX/MXD 网络成员

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-739552|uniprotkb:Q5ETU4|uniprotkb:Q6ZRZ5|ensembl:ENSP00000347358.5 | MI:0398(two hybrid pooling approach | PMID:pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | — | — |
| intact:EBI-945833|intact:EBI-2859688|uniprotkb:Q5BKT8|uniprotkb:Q5VTG9|uniprotkb:Q5XG84|uniprotkb:Q6P192|uniprotkb:Q8NC23|uniprotkb:Q8WUQ9|uniprotkb:Q96FY1|ensembl:ENSP00000354929.6|ensembl:ENSP00000508809.1|ensembl:ENSP00000510366.1|ensembl:ENSP00000510377.1 | MI:0397(two hybrid array) | PMID:imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 | — | — |
| intact:EBI-741574|uniprotkb:Q53HK1|uniprotkb:Q7Z4Y0|uniprotkb:Q8NDJ7|uniprotkb:Q96ME3|ensembl:ENSP00000401867.2|ensembl:ENSP00000421463.1|uniprotkb:B4E0J1 | MI:1112(two hybrid prey pooling app | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-347978|intact:EBI-28983799|uniprotkb:Q6GTM2|uniprotkb:Q503A4|uniprotkb:Q96C43|uniprotkb:Q9NSL1|uniprotkb:B3KWU5|ensembl:ENSP00000305503.3|ensembl:ENSP00000407331.1|ensembl:ENSP00000468839.2|ensembl:ENSP00000468842.2|ensembl:ENSP00000468884.2|ensembl:ENSP00000471191.1|ensembl:ENSP00000473192.1|ensembl:ENSP00000515006.1|ensembl:ENSP00000515007.1|ensembl:ENSP00000515008.1|ensembl:ENSP00000515009.1|ensembl:ENSP00000515010.1|ensembl:ENSP00000515011.1|ensembl:ENSP00000515012.1|ensembl:ENSP00000515013.1|ensembl:ENSP00000515014.1 | MI:1356(validated two hybrid) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-21639435 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| MAX | 0.0 | — | — |
| SIN3A | 0.0 | — | — |
| MNT | 0.0 | — | — |
| SAP30 | 0.0 | — | — |
| SUDS3 | 0.0 | — | — |
| ING2 | 0.0 | — | — |
| MXI1 | 0.0 | — | — |
| SAP30L | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 5
- 调控相关比例: 3/15 (20%)

**评价**: PPI 得分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=73.4, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/5/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nuclear membrane, Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 有一定研究基础 (PubMed 54 篇)，几乎未被研究
2. HPA 确认核定位，中等置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MXD3
- Protein Atlas: https://www.proteinatlas.org/MXD3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MXD3
- UniProt: https://www.uniprot.org/uniprotkb/Q9BW11
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BW11


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MXD3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MXD3/MXD3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BW11 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 57..109; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR036638; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213347-MXD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TFIP11 | Intact, Biogrid | true |
| CYSRT1 | Intact | false |
| KRT31 | Intact | false |
| KRTAP1-1 | Intact | false |
| KRTAP1-3 | Intact | false |
| KRTAP10-7 | Intact | false |
| KRTAP3-3 | Intact | false |
| MAX | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
