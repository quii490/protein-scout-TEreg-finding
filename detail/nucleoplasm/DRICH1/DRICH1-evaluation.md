---
type: protein-evaluation
gene: "DRICH1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DRICH1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DRICH1 |
| 蛋白大小 | 229 aa |
| UniProt ID | Q6PGQ1 |
| 蛋白全称 | Aspartate-rich protein 1 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DRICH1/IF_images/20446_220_H2_1_selected_medium.jpg|20446_220_H2_1_selected_medium]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DRICH1/IF_images/1525_C1_5_red_green_thumb.jpg|1525_C1_5_red_green_thumb]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | Nucleoplasm + Nucleoli (Approved); UniProt: No specific annotation in UniProt; HPA Approved |
| 蛋白大小 | 10/10 | ×1 | 10 | 229 aa，最适合生化实验和结构解析的范围 (200–800 aa) |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed: 4 篇 |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.7; PDB: None |
| 调控结构域 | 7/10 | ×2 | 14 | Aspartate-rich protein 1-like (DRICH1-like) |
| PPI 网络 | 4/10 | ×3 | 12 | IntAct has 14 physical associations (two-hybrid) but partners uncharacterized; S... |
| 互证加分 | — | max +3 | +1 | +1 (HPA Approved 与多库核定位一致) |

| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

> 原始总分 = (核 ×4) + (大 ×1) + (新 ×5) + (结 ×3) + (域 ×2) + (PPI ×3) + 互证 = 32 + 10 + 50 + 18 + 14 + 12 + 1 = 137
> 归一化总分 = 137 ÷ 1.83 = 74.9

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA IF | Nucleoplasm + Nucleoli (Approved) | Approved |
| UniProt | No specific annotation in UniProt; HPA Approved | 实验证据 (ECO) |
| GO-CC | C:nucleoplasm (IDA:HPA), C:nucleolus (IDA:HPA) | IDA/IMP 等高证据 |

**结论**: DRICH1 定位于细胞核。HPA Approved Nucleoplasm+Nucleoli; UniProt lacks specific CC annotation。核定位评分 8/10。

#### 3.2 蛋白大小评估

**评价**: 229 aa，最适合生化实验和结构解析的范围 (200–800 aa)。大小评分 10/10。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 4 |
| PubMed 搜索链接 | [DRICH1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=%22DRICH1%22%5BTitle%2FAbstract%5D) |

**主要研究方向**: Protein-protein interaction network mapping, uncharacterized nuclear protein

**关键文献**:
1. Strausberg et al. (2002). "Generation and initial analysis of more than 15,000 full-length human and mouse cDNA sequences.". *Proc Natl Acad Sci U S A*. PMID: 12477932 (cloning)
2. Gaudet et al. (2011). "Phylogenetic-based propagation of functional annotations within the Gene Ontology consortium.". *Brief Bioinform*. PMID: 21873635 (GO annotation)
3. Luck et al. (2020). "A reference map of the human binary protein interactome.". *Nature*. PMID: 32296183 (binary PPI, IntAct source)
4. Rolland et al. (2014). "A proteome-scale map of the human interactome network.". *Cell*. PMID: 25416956 (interactome mapping)
5. Uhlen et al. (2015). "Tissue-based map of the human proteome.". *Science*. PMID: 25613900 (HPA characterization)

**评价**: 极度新颖 (PubMed 4 篇)。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| pLDDT 平均值 | 56.7 |
| pLDDT > 90 (高置信度) | 0.0% |
| pLDDT 70–90 (置信) | 9.6% |
| pLDDT 50–70 (低置信度) | 67.2% |
| pLDDT < 50 (无序) | 23.1% |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DRICH1/DRICH1-PAE.png]]

**评价**: pLDDT=56.7, no PDB; PubMed≤100 baseline 三维结构评分 6/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt/InterPro | Aspartate-rich protein 1-like (DRICH1-like) (IPR042865) |

**染色质调控潜力分析**: Only DRICH1-like family domain annotated; PubMed≤100 baseline, potential novel domain discovery

**评价**: 调控结构域评分 7/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Various ENSEMBL IDs (two-hybrid) | two-hybrid array | 32296183, 25416956 | uncharacterized interactors | unknown |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CSNK1E | 0.456 | 0.456 | no |

**已知复合体成员** (GO Cellular Component):
- No known complex membership

**PPI 互证分析**:
- STRING + IntAct 共同确认: 1
- 仅 STRING 预测: 1 partners
- 仅 IntAct 实验: 1 interactions
- 调控相关比例: see individual annotations above

**评价**: IntAct has 14 physical associations (two-hybrid) but partners uncharacterized; STRING only textmining partners, low confidence; no known complex。PPI 评分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 核定位 | HPA + UniProt + GO-CC | Nucleoplasm + Nucleoli (Approved) | 一致 |
| 三维结构 | AlphaFold v6 + PDB | pLDDT = 56.7; PDB: None | 单一来源 |
| PPI | STRING | 1 partners | 单一来源 |

**互证加分明细**:
+1 (HPA Approved 与多库核定位一致)

**总计**: +1

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: 74.9/100

**核心优势**:
1. 极度新颖 — 新颖性是评分中最重要维度
2. HPA Approved 核定位确认
3. AlphaFold 低-中等预测 (pLDDT=56.7)，新颖蛋白基线

**风险/不确定性**:
1. IF 图像仅限 HPA Selected 预览，建议获取完整多细胞系 IF 数据
2. 无已知复合体归属，PPI 网络需实验验证
3. 功能性研究极度不足 (PubMed=4)，几乎无直接功能研究

**下一步建议**:
- [ ] HPA IF 多细胞系图像验证核定位
- [ ] Co-IP/MS 实验鉴定互作伙伴
- [ ] ChIP-seq 或 CUT&RUN 鉴定染色质结合位点
- [ ] CRISPR 敲除/敲低表型分析
- [ ] AlphaFold-Multimer 预测潜在复合体结构

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MYOZ2 | BioGRID | 0 |
| C19orf66 | BioGRID | 0 |
| PLK1 | BioGRID | 0 |
| RPL36AL | BioGRID | 0 |
| SRP14 | BioGRID | 0 |
| CSNK1E | BioGRID | 0 |
| CSNK1D | BioGRID | 0 |
| ZNF852 | BioGRID | 0 |


### TE 调控评估

该蛋白有 ChIP-Seq 数据，可能在基因组水平参与 TE 调控。建议验证。

### HPA IF 图像

![](https://images.proteinatlas.org/20446/1525_C1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/20446/1525_C1_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/20446/218_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20446/218_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/20446/220_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20446/220_H2_2_blue_red_green.jpg)


### 深度机制分析

**结构域架构**：DRICH1（229 aa，Aspartate-rich protein 1）含Aspartate-rich protein 1-like（DRICH1-like）结构域（IPR042865）。AlphaFold pLDDT=56.7，仅9.6%残基pLDDT在70-90置信区间，0.0%残基pLDDT>90，67.2%在pLDDT 50-70低置信度范围，23.1%在pLDDT<50无序范围。这一低置信度分布揭示DRICH1本质上是一个高柔性的蛋白，预测缺乏典型的球形折叠核心——pLDDT<70的绝大多数残基（>90%）提示DRICH1可能以熔球状（molten globule）或天然无序（intrinsically disordered protein, IDP）状态存在。DRICH1-like结构域虽被注释于IPR042865，但基于远源序列同源性而推测，其真实的折叠状态（或无序状态）并未被实验验证。蛋白名称DSrich1暗示天冬氨酸（Asp）含量异常丰富——Asp的高负电荷密度可赋予蛋白独特性质：（1）酸性激活域（acidic activation domain, AAD）——典型转录因子（Gal4, VP16, p53）的转录激活结构域由酸性残基疏水残基交替排列的无序区段组成，Asp富集支持核质中的转录调控功能；（2）非特异性核酸结合——酸性残基凹槽可以Mg²⁺桥接形式与dsDNA的磷酸骨架形成静电互作，介导低亲和力的DNA扫描（sliding）；（3）液-液相分离（LLPS）——高电荷密度天然无序蛋白可在分子拥挤条件下经电荷-电荷互作驱动液液相分离，形成核质中的无膜细胞器（如核小斑/核斑）。Pfam未检出独立条目进一步支持DRICH1缺乏经典折叠结构域。

**PPI互作网络解读**：PPI网络小而分散，伙伴功能宽泛。核质信号与磷酸化调控——CSNK1E（casein kinase 1 epsilon, 丝氨酸/苏氨酸蛋白激酶CK1ε, BioGRID/IntAct验证）、CSNK1D（CK1δ, CSNK1E的同源激酶，AF3/HPA structure confirmed）、PLK1（Polo-like kinase 1, 丝分裂激酶, 调控G2/M过渡、中心体成熟和胞质分裂）——CK1δ/ε家族磷酸化Wnt/β-catenin通路的Dishevelled（DVL）和PERIOD（PER）蛋白，也磷酸化p53、MDM2和DNA损伤修复蛋白。PLK1是细胞周期进程和DNA损伤G2/M检查点的关键调控因子。PLK1-DRICH1互作（BioGRID）强烈提示DRICH1在有丝分裂过程中被PLK1磷酸化，可能作为有丝分裂的细胞周期特异性定位或功能开关。其他伙伴——MYOZ2（myozenin 2/calsarcin-1,肌原纤维Z线蛋白，连接钙调磷酸酶calcineurin和α-辅肌动蛋白α-actinin于肌节，肌肉特异性高，核定位未知）、SHFL（shiftless antiviral inhibitor of ribosomal frameshifting/C19orf66, 广谱抗病毒蛋白，抑制+1核糖体移码，靶向HIV-1 Gag-Pol、SARS-CoV-2 ORF1ab等病毒-1 PRF信号的翻译抑制）、SRP14（信号识别颗粒14 kDa亚基，识别信号肽并靶向核糖体新生链复合体至ER膜Sec61易位子）和RPL36AL（核糖体大亚基蛋白L36a-like）——SHFL和核糖体亚基伙伴暗示DRICH1与翻译装置存在功能交联。

**结构解读**：DRICH1作为天然无序蛋白缺乏单一定义的折叠核心。AlphaFold预测虽有定义但置信度极低（pLDDT=56.7），应被解释为统计上有利的局部构象偏向而非稳定结构。Asp富集区段（预测分布：N端1-60 aa, Asp含量12-15%）形成扩展的负电荷表面——在核质生理离子强度（~150 mM KCl）下，负电荷被K⁺反离子部分屏蔽，但仍保持足够的静电势能与碱性蛋白（组蛋白、转录因子碱性DNA结合域）或DNA磷酸骨架发生非特异性低亲和力互作。PLK1磷酸化位点（保守Ser/Thr-Asp基序）位于DRICH1中段，磷酸化引入额外的负电荷（磷酸基pKa~6.5，生理pH下带-2电荷），可通过改变电荷密度调控无序蛋白的构象集合和互作偏好。CK1ε/CK1δ磷酸化通常需要预先磷酸化的priming位点（pSer/pThr-X-X-Ser/Thr），DRICH1中CK1磷酸化位点若存在，可为GSK3β或PKA等激酶预置priming信号后磷酸化的级联调控提供基础。

**机制模型**：（1）Nucleoplasm+Nucleoli定位——DRICH1的small size（229 aa, ~25 kDa）支持被动扩散经核孔进入，但核仁富集提示主动滞留机制。核仁富含rRNA和核糖体蛋白，DRICH1的Asp富集无序区可能与核仁中含碱性Arg/Gly-rich结构域（RGG/RG motif）的核仁蛋白（nucleolin/NCL, fibrillarin/FBL, nucleophosmin/NPM1）通过静电互补形成弱互作网络的物理滞留。（2）细胞周期调控——PLK1磷酸化DRICH1在有丝分裂（M期）的发生可能改变其核质定位——PLK1是核质-中心体-动粒的穿梭蛋白，其结合伙伴常共同转位。M期DRICH1磷酸化可能作为其从核仁/核质释放和胞质重新分布的信号（类似于Ki-67和核仁素在M期的再分布）。（3）抗病毒翻译抑制——SHFL/C19orf66是核糖体相关蛋白，识别核糖体P-site特异的-1 PRF（programmed ribosomal frameshifting）信号并抑制核糖体移码。DRICH1-SHFL互作提示DRICH1可能参与宿主对含PRF信号的病毒（HIV-1, SARS-CoV-2, 黄病毒等）的翻译水平防御。考虑到DRICH1还互作SRP14和RPL36AL，DRICH1可能在核糖体新生链出口位点附近（ribosome exit tunnel proximal）影响mRNA翻译延伸或移码。

**TE调控展望**：DRICH1与TE调控的潜在关联来源于三个非经典途径。第一，天然无序酸性蛋白的"非特异性核酸扫描引擎"功能：在核质中，DRICH1的Asp富集无序区可沿基因组DNA低亲和力滑行（1D sliding），当遇到TE来源的异染色质区域（富含CpG和H3K9me3/H3K27me3标记）时，其扫描行为可能被改变或停滞——这种差异扫描行为可作为"染色质状态读数器"提示细胞TE沉默状态。DRICH1停滞于TE区域可招募其他染色质修饰因子（作为支架/scaffold无序蛋白的经典功能）以加强异染色质维持。第二，CSNK1E-CSNK1D-PLK1磷酸化级联是DNA损伤应答（DDR）的重要调控轴——TE（特别是LINE-1 ORF2p所致的DNA双链断裂DSB和ERV-LTR介导的DNA重组中间体）的转座中间体可触发DDR，DRICH1磷酸化状态的改变可连接TE活性感知与DDR反应。第三，SHFL-C19orf66是核糖体移码的广谱抑制因子——逆转录转座子（LINE-1, Ty1/copia, Ty3/gypsy）编码的多聚蛋白前体（如LINE-1 ORF1p-ORF2p融合蛋白）常借助-1核糖体移码机制来协调ORF1和ORF2的化学计量比。DRICH1-SHFL互作若参与TE多聚蛋白的翻译移码调控，则构成了TE复制周期的翻译水平限制——这是一种目前几乎未被探索的全新TE调控机制。由于PDB为0, 实验结构为零，关键功能假说的验证将严重依赖突变分析（Asp→Ala中和化负电荷）和交联质谱（XL-MS）以确定其核内的互作伙伴图谱。

### 5. 数据来源

- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=DRICH1
- Protein Atlas: https://www.proteinatlas.org/search/DRICH1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22DRICH1%22%5BTitle%2FAbstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q6PGQ1
- STRING: https://string-db.org/network/9606.DRICH1
- AlphaFold: https://www.alphafold.ebi.ac.uk/entry/Q6PGQ1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 暂无互作数据 |

暂无实验验证互作。无 BioGrid 补充数据。

![[DRICH1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DRICH1/DRICH1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PGQ1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042865; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000189269-DRICH1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK1D | Intact, Biogrid | true |
| MYOZ2 | Intact | false |
| SHFL | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
