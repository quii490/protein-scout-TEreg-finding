---
type: protein-evaluation
gene: "MROH1"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MROH1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MROH1 |
| 别名 | HEATR7A |
| 基因全称 | maestro heat like repeat family member 1 |
| 蛋白名称 | Maestro heat-like repeat-containing protein 1 |
| 蛋白大小 | 1641 aa |
| UniProt ID | Q8NDA8 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm (IDA supported) |
| Size 蛋白大小 | 5/10 | x1 | 5 | 1641 aa |
| Novelty 研究新颖性 | 10/10 | x5 | 50 | PubMed: 3 篇 |
| 3D Structure 三维结构 | 8/10 | x3 | 24 | AlphaFold pLDDT=84.2 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含 HEAT repeat，参与蛋白-蛋白互作 |
| PPI Network PPI网络 | 4/10 | x3 | 12 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
| **原始总分** |  |  | **142/183** |  |
| **归一化总分** |  |  | **77.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | RT-4, MCF-7 | HPA validated |
| UniProt | Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IBA|IDA|IEA|NAS) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MROH1/IF_images/MCF_7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MROH1/IF_images/RT_4_1.jpg|RT-4]]
#### 3.2 蛋白大小评估

1641 aa，较大的蛋白

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 3 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Li L et al. (2024). "The HEAT repeat protein HPO-27 is a lysosome fission factor.". *Nature*. PMID: 38538795
2. Thomason PA et al. (2017). "Mroh1, a lysosomal regulator localized by WASH-generated actin.". *J Cell Sci*. PMID: 28424231
3. Jayawardana JMDR et al. (2023). "Genomic Regions Associated with Milk Composition and Fertility Traits in Spring-Calved Dairy Cows in New Zealand.". *Genes (Basel)*. PMID: 37107618
4. Alfahed A et al. (2023). "Prognostic Values of Gene Copy Number Alterations in Prostate Cancer.". *Genes (Basel)*. PMID: 37239316
5. Sharbatoghli M et al. (2022). "Copy Number Variation of Circulating Tumor DNA (ctDNA) Detected Using NIPT in Neoadjuvant Chemotherapy-Treated Ovarian Cancer Patients.". *Front Genet*. PMID: 35938032


**评价**: PubMed 3 篇，属极度新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 84.2 |
| pLDDT > 90 占比 | 27.6% |
| pLDDT 70-90 占比 | 63.7% |
| pLDDT 50-70 占比 | 5.5% |
| pLDDT < 50 占比 | 3.2% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MROH1/MROH1-PAE.png]]

**评价**: AlphaFold 预测高质量，整体折叠良好 (AlphaFold v6, pLDDT=84.2, >90=28%, 70-90=64%, 50-70=6%, <50=3%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含 HEAT repeat，参与蛋白-蛋白互作

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-4282243|uniprotkb:Q3TNK4|uniprotkb:Q8K306|ensembl:ENSMUSP00000023535.4 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:21565611|imex:IM-16529 | — | — |
| intact:EBI-1257123 | MI:0096(pull down) | PMID:pubmed:19367725|imex:IM-20587 | — | — |
| intact:EBI-10763431|uniprotkb:B3KUS1|uniprotkb:Q502X8|ensembl:ENSP00000326579.4|ensembl:ENSP00000370139.4|ensembl:ENSP00000370140.3 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:26496610|imex:IM-24272 | — | — |
| intact:EBI-2553777|uniprotkb:A2ARS1|ensembl:ENSMUSP00000037126.8 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:26496610|imex:IM-24272 | — | — |
| intact:EBI-11021342|uniprotkb:Q91YL5|uniprotkb:Q3UE33|uniprotkb:Q9CV50|uniprotkb:Q9JIG6|ensembl:ENSMUSP00000033494.10 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:26496610|imex:IM-24272 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CYHR1 | 0.0 | — | — |
| CPSF1 | 0.0 | — | — |
| ARHGAP39 | 0.0 | — | — |
| FAM83H | 0.0 | — | — |
| PPP1R16A | 0.0 | — | — |
| ADCK5 | 0.0 | — | — |
| MAPK15 | 0.0 | — | — |
| GPAA1 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 19
- 调控相关比例: 2/15 (13%)

**评价**: PPI 得分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=84.2, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/19/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- GO-CC IDA 实验证据 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★ (4/5)

**核心优势**:
1. 极度新颖 (PubMed 3 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MROH1
- Protein Atlas: https://www.proteinatlas.org/MROH1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MROH1
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDA8
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDA8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MROH1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MROH1/MROH1-PAE.png]]




